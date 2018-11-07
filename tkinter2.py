#!/usr/bin/env python
#coding=utf-8

from Tkinter import *
root = Tk() #创建窗口对象的背景色

li = ['C','python','php','html','SQL','JAVA']
movie = ['CSS','jQuery','Bootstrap']
listb = Listbox(root)  #创建两个列表组件
listb2 = Listbox(root)
for item in li: #第一个部件插入数据
    listb.insert(0,item)

for item in movie:
    listb2.insert(0,item)

listb.pack()    #将小部件放置到主窗口中
listb2.pack()
root.mainloop()