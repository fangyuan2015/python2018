#!/usr/bin/env python
#coding=utf-8

#可写函数说明
def printinfo(name,age=35):
    "打印任何传入的字符串"
    print "Name:",name
    print "Age:",age
    return

#调用printinfo函数
printinfo(age=50,name="miki")
printinfo(name='fangyuan')
