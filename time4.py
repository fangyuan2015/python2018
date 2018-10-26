#!/usr/bin/env python
#coding=utf-8

import time 

print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
#格式化成2018-10-26 11:28:30形式

print time.strftime("%a %b %d %H:%M:%S %Y",time.localtime())
#格式化成Sat Mar 28 22:22:22形式

a = 'Sat Mar 28 22:22:22 2016'
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
