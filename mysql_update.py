#!/usr/bin/env python
#coding=utf-8

import MySQLdb

#打开数据库连接
db = MySQLdb.connect('localhost','testuser','test123!','TESTDB',charset='utf8')

#获取数据库游标
cursor = db.cursor()

#SQL语句更新
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
    #执行sql语句
    cursor.execute(sql)
    #提交到数据库执行
    db.commit()
except:
    #发生错误时回滚
    db.rollback()

#关闭数据库连接
db.close()
