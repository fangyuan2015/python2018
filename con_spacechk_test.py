#!/usr/bin/env python
#coding:utf-8
#Date:2017/9/15
#Version:0.1
#description:用户检查开发环境web容器的磁盘空间大小并通过delet.sh脚本清理日志

import os,sys

AVIMEM = os.popen("docker exec -i D-LT-Nginx-Tomcat-100 df -h /|awk 'NR>1{print $3}'").readlines()[1]
print "D-LT-Nginx-Tomcat-100 可用/分区空间为 %s" % (AVIMEM,)


AVIMEM = os.popen("docker exec -i D-LT-Nginx-Tomcat-102 df -h /|awk 'NR>1{print $3}'").readlines()[1]
print "D-LT-Nginx-Tomcat-102 可用/分区空间为 %s" % (AVIMEM,)

#检查容器系统的定时任务服务是否启动
contain1 = "D-LT-Nginx-Tomcat-100"
contain2 = "D-LT-Nginx-Tomcat-102"
print  contain1,"定时计划任务",os.popen("docker exec -i D-LT-Nginx-Tomcat-100 /etc/init.d/crond status|awk '{print $4}'").readlines()[0]
print  contain2,"定时计划任务",os.popen("docker exec -i D-LT-Nginx-Tomcat-102 /etc/init.d/crond status|awk '{print $4}'").readlines()[0]

#手动清理容器系统Tomcat日志内容
#choice = raw_input("是否执行容器中Tomcat日志清理工作，请输入y 或 n: ").lower()
#if choice == 'y':
act1 = os.system("docker exec -i D-LT-Nginx-Tomcat-100 sh /SSY/delet.sh")
print "清理D-LT-Nginx-Tomcat-100容器的日志完成"
AVIMEM = os.popen("docker exec -i D-LT-Nginx-Tomcat-100 df -h /|awk 'NR>1{print $3}'").readlines()[1]
print "D-LT-Nginx-Tomcat-100 可用/分区空间为 %s" % (AVIMEM,)

act1 = os.system("docker exec -i D-LT-Nginx-Tomcat-102 sh /SSY/delet.sh")
print "清理D-LT-Nginx-Tomcat-102容器的日志完成"
AVIMEM = os.popen("docker exec -i D-LT-Nginx-Tomcat-102 df -h /|awk 'NR>1{print $3}'").readlines()[1]
print "D-LT-Nginx-Tomcat-100 可用/分区空间为 %s" % (AVIMEM,)
#else:
#    print "你选择了不清理容器Tomcat的日志内容"







