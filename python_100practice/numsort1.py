#!/usr/bin/env python
#coding=utf-8

#有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
li = []
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                s = str(i)+str(j)+str(k)
                li.append(s)

print li
print "元素个数为：",len(li)

