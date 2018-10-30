#!/usr/bin/env python
#coding=utf-8

import os

document = open("testfile.txt","w+")
print "文件名：",document.name
document.write("这是我创建的第一个测试文件！\nwelcome!")
print document.tell()
#输出当前指针
document.seek(os.SEEK_SET)
#设置指针回到文件最初
context = document.read()
print context
document.close()
