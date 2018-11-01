#!/usr/bin/env python
#coding=utf-8

class Vector:
    def __init__(self,a,b):
	self.a = a
	self.b = b

    def __str__(self):
	return "Ve1tor (%d,%d)" % (self.a,self.b)

    def __add__(self,other):
	print other
	return Vector(self.a + other.a,self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print "v1:",v1
print "v2:",v2
print v1 + v2
