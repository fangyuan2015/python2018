#!/usr/bin/env python
#coding=utf-8

class Employee:
    "所有员工的基类"
    empCount = 0
   
    def __init__(self,name,salary):
        self.name = name
	self.salary = salary
	Employee.empCount += 1

    def dsplayCount(self):
	print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
	print "Name:",self.name,",Salary:",self.salary
