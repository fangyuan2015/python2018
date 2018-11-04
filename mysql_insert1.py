#!/usr/bin/env python
#coding=utf-8

import MySQLdb

db = MySQLdb.connect("localhost",'testuser','test123!','TESTDB',charset='utf8')

#使用cursor()获取操作游标
cursor = db.cursor()

#SQL插入语句
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
	LAST_NAME,AGE,SEX,INCOME) VALUES ( \
	'%s','%s','%d','%s','%d')" % ('Mac','Mohan',20,'M',2000)

try:
    #执行sql语句
    cursor.execute(sql)
    #提交到数据库执行
    db.commit()
except:
    #发生错误时回滚
    db.rollback()

