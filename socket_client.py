#!/usr/bin/env python
#coding=utf-8

import socket	#导入socket模块

s = socket.socket()	#创建socket对象
host = socket.gethostname()	#获取本地主机名
port = 12345	#设置端口号

s.connect((host,port))
print s.recv(1024)
s.close()
