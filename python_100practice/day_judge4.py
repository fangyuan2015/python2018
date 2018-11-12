#!/usr/bin/env python
#coding=utf-8
#输入某年某月某日，判断这一天是这一年的第几天？
year = int(raw_input('请输入年份：'))
month = int(raw_input('请输入月份：'))
day = int(raw_input("请输入日期："))

if year % 4 == 0 or year % 100 == 0 :
    if month > 2:
            
    else:
        day_position = (month -1) * 31 + day
        print "the day is the %d",% day_position
else:
    
    
