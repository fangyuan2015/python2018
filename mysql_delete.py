#!/usr/bin/env python
#coding=utf-8

import MySQLdb

#连接数据库
db = MySQLdb.connect('localhost','testuser','test123!','TESTDB',charset='utf8')

#获取数据库游标
cursor = db.cursor()

#SQL删除语句
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

#关闭数据库连接
db.close()
