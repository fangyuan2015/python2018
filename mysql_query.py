#!/usr/bin/env python
#coding=utf-8

import MySQLdb

#创建数据库连接
db = MySQLdb.connect("localhost",'testuser','test123!','TESTDB',charset='utf8')

#获取操作游标
cursor = db.cursor()

#SQL查询语句
sql = "SELECT * FROM EMPLOYEE WHERE INCOME > '%d'" % (1000)

try:
    cursor.execute(sql)
    #获取所有的操作记录
    results = cursor.fetchall()
    for row in results:
  	fname = row[0]
	lname = row[1]
	age = row[2]
	sex = row[3]
	income = row[4]
	print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
	(fname,lname,age,sex,income)
except:
    print "Error:unable to fecth data"
