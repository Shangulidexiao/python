#!/usr/bin/env python
# -*- coding:utf-8 -*-

"13章练习题"

# 13.1


# 13.2
方法是在类内定义的函数，只能由实例调用

# 13.3
def dollarize(money):
	if isinstance(money,(float,int)):
		fu,m = '','$'
		if money < 0:
			fu = '-'
		f = str(abs(money)).split('.')
		try:
			return fu + m + addcomma(f[0]) + '.' + f[1][:2]
		except IndexError:
			return fu + m + addcomma(f[0]) + '.00'
	else:
		raise TypeError('please input a float')
	
 
def addcomma(numStr):
	if int(numStr) < 999:
		return numStr
	length = len(numStr) % 3
	retval = numStr[:length]+','
	newstr = numStr[length:]
	for i,s in enumerate(newstr):
		if (i+1) % 3 == 0:
			retval += s+',' 
		else:
			retval += s
	return retval.strip(',')

# 13.5
class Point(object):
	def __init__(self,x=0,y=0):
		self.__x = x
		self.__y = y
	def __str__(self):
		return str((self.__x,self.__y))	
	def __repr__(self):
		return str((self.__x,self.__y))

#13.6
class Line(object):
	def __init__(self,x=0,y=0):
		self.__x = x
		self.__y = y
	def __str__(self):
		return str((self.__x,self.__y))	
	def __repr__(self):
		return str((self.__x,self.__y))