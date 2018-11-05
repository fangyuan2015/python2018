#!/usr/bin/env python
#coding=utf-8

import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

sender = 'from@runoob.com'
receivers = ['546219618@qq.com'] #接收邮件，可以设置为你的邮箱

msgRoot = MIMEMultipart('related')
msgRoot['From'] = Header('菜鸟教程','utf-8')
msgRoot['To'] = Header('测试','utf-8')
subject = 'Python SMTP邮件测试'
msgRoot['Subject'] = Header(subject,'utf-8')

msgAlternative = MIMEMultipart('alterantive')
msgRoot.attach(msgAlternative)

mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">菜鸟教程链接</a></p>
<p>图片演示：</p>
<p><img src="cid:image1"></p>
"""

msgAlternative.attach(MIMEText(mail_msg,'html','utf-8'))

#指定图片为当前目录
fp = open('test.png','rb')
msgImage = MIMEImage(fp.read())
fp.close()

#定义图片ID,在HTML文本中引用
msgImage.add_header('Content-ID','<image1>')
msgRoot.attach(msgImage)

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender,receivers,msgRoot.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"

