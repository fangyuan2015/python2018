#!/usr/bin/env python
#coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header

#第三方SMTP服务
mail_host="smtp.XXX.com"	#设置服务器
mail_user="aaa"	#用户名
mail_pass="xxx" #口令

sender = 'from@runoob.com'
receivers = ['546219618@qq.com']	#接收邮件，可设置为你的qq邮箱或者其他邮箱

message = MIMEText('Python 邮件发送测试。。。','plain','utf-8')
message['From'] = Header("菜鸟教程",'utf-8')
message['To'] = Header("测试",'utf-8')

subject = 'Python SMTP邮件测试'
message['Subject'] = Header(subject,'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host,25)	#25为SMTP端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender,receivers,message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"
