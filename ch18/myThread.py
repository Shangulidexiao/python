#! /usr/bin/env python
# -*- coding:utf-8 -*-

"自定义线程类"

from threading import Thread
from time import sleep,ctime

class MyThread(Thread):
	def __init__(self,func,args,name):
		super(self.__class__,self).__init__()
		self.name = name
		self.func = func
		self.args = args
	def run(self):
		print 'starting',self.name,'at:', ctime()
		self.res = self.func(*self.args)
		print self.name,'finished at:', ctime()
	def getResult(self):
		return self.res

if __name__ == '__main__':
	def hello(fu,num):
		print fu * num
	t = myThread(hello,('-',30),hello.__name__)
	t.start()
