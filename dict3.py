#!/usr/bin/env python
#coding=utf-8

dict = {'Name':'Zara','Age':7,'Class':'First'}

del dict['Name'] #删除键是name的条目
dict.clear() #清空词典所有条目
del dict #删除词典

print "dict['Age']:",dict['Age']
print "dict['School']:",dict['School']
