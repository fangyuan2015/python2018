#!/bin/bash
#Filename：oth_war_deploy.sh
#description：此版本可以同时用于微贷和小富环境无tms，dir_ssy包部署
#date:2018/5/18

DATE=`date +%F`
DEPLOY_DIR=/SSY/Deploy/$DATE
BACKUP_DIR=/SSY/Backup/$DATE
OLDWAR_DIR=/SSY/tomcat8/webapps
TEMP_DIR=/SSY/Deploy
TOMCAT_PID=`ps -ef|grep -v grep |grep tomcat8|awk '{print $2}'`
TOMCAT_PID_NUM=`ps -ef|grep -v grep |grep tomcat8|awk '{print $2}'|wc -l`

if [ ! -d ${DEPLOY_DIR} ];then
        mkdir -p ${DEPLOY_DIR}
fi

if [ ! -d ${BACKUP_DIR} ];then
        mkdir -p ${BACKUP_DIR}
fi
#定义和创建更新与备份目录

/bin/cp ${TEMP_DIR}/*.war ${DEPLOY_DIR}
#将Jenkins中上传目录中的war包拷贝到部署目录中

if [ ! -f /tmp/fail_deploy.log ];then
	touch /tmp/fail_deploy.log
fi

>/SSY/tomcat8/logs/catalina.out
#清空tomcat日志
>/tmp/fail_deploy.log
>/tmp/success_deploy.log

if [ ! -f ${DEPLOY_DIR}/tms.war ] && [ ${TOMCAT_PID_NUM} -ge 1 ];then
	kill -9 ${TOMCAT_PID}
	echo "本服务器上无tms部署,先停止tomcat进程"
	if [ ${TOMCAT_PID_NUM} -eq 0 ];then
		echo "tomcat 进程停止成功，开始接下来的拷贝和备份"
	fi
fi


if [ -f ${DEPLOY_DIR}/tms.war ];then
	/bin/cp ${DEPLOY_DIR}/dir.war ${DEPLOY_DIR}/dir_ssy.war
fi

if [ `ls -l /SSY/tomcat8/webapps/*.war|wc -l` -ge 1 ];then
        /bin/cp /SSY/tomcat8/webapps/*.war ${BACKUP_DIR}
else
        echo "/SSY/tomcat8/webapps dir has no war file"
       
fi
#备份/SSY/tomcat8/webapps/*.war 包

for j in `ls -l ${OLDWAR_DIR}/*.war|awk '{print $9}'|awk -F '/' '{print $5}'|awk -F '.' '{print $1}'`
do
	/bin/cp ${OLDWAR_DIR}/$j /tmp
        rm -rf ${OLDWAR_DIR}/$j
        rm -f ${OLDWAR_DIR}/*.war
done
echo "清空tomcat中已有的旧包"
echo "${OLDWAR_DIR} content"
ls ${OLDWAR_DIR}
#请空OLDWAR_DIR=/SSY/tomcat8/webapps目录中旧的war包及相关文件夹

echo "完成包的备份和拷贝 开始启动 tomcat 进行部署"

if [ ! -f ${DEPLOY_DIR}/tms.war ];then
	/etc/init.d/tomcat start
	if [ ${TOMCAT_PID_NUM} -gt 0 ];then
		echo "tomcat 启动成功，开始进行部署"
	fi
fi
#判断，如果部署目录中无tms.war包说明此为小富机器，需要启动tomcat，否则则为含tms.war包机器无需启动tomcat

for i in `ls -l ${DEPLOY_DIR}/*.war|awk '{print $9}'|awk -F '/' '{print $5}'`
#i 指遍历${DEPLOY_DIR}目录中每一个war包名
do
        /bin/cp ${DEPLOY_DIR}/$i ${OLDWAR_DIR}
        seconds_left=240
        while [ $seconds_left -gt 0 ]
        do
                sleep 5
                com_log=`grep "$i has finished" /SSY/tomcat8/logs/catalina.out`
                com_log_item=`grep "$i has finished" /SSY/tomcat8/logs/catalina.out|wc -l`
                com_error_log=`grep  "ERROR" /SSY/tomcat8/logs/catalina.out`
                com_error_log_item=`grep "ERROR" /SSY/tomcat8/logs/catalina.out|wc -l`
                if [ $com_error_log_item -ge 1 ];then
                        echo "------------------------------"
                        echo "take care error log:"
						echo "------------------------------"
                        echo $com_error_log
						echo $HOSTNAME >>/tmp/fail_deploy.log
                        echo "$i has error" >>/tmp/fail_deploy.log
						echo ${com_error_log}>>/tmp/fail_deploy.log
                        break
                elif [ $com_log_item -ge 1 ];then
                        echo $com_log
						echo $HOSTNAME>>/tmp/success_deploy.log
                        echo $com_log >>/tmp/success_deploy.log
                        #将成功部署war包日志记录
                        echo "--------------------------------"
                        echo "$i success deploy complete "
                        echo "--------------------------------"
                        break
                else
                        echo "$i deploying,please wait "
			seconds_left=$(($seconds_left - 5))
			if [ $seconds_left -lt 0 ];then
				echo "请检查WEB页面，以确认部署是否成功"
				break
			else
				continue
			fi
                fi
        done
done

#rm -f ${TEMP_DIR}/*.war
#清空中转文件夹中war包

echo "Deploy process finished"
echo " "
echo "-----------------------------"
echo "Maybe Deploy faile war list: "
if [ -s /tmp/fail_deploy.log ];then
        cat /tmp/fail_deploy.log
else
        echo "部署过程中未检测到部署失败日志内容，初步确定包均以部署成功"
fi

echo "-----------------------------"
echo "Deploy success war list"
echo "-----------------------------"
cat /tmp/success_deploy.log

