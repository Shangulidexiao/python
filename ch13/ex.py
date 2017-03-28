#!/usr/bin/env python
# -*-coding:utf-8 -*-

"类对象练习"

class Foo(object):
	"test"
	myVersion = '1.1'
	def __init__(self):
		print 'create by init'
	def __del__(self):
		print 'delete by del'
	@staticmethod
	def myMoActionMethon():
		print Foo.myVersion



class P(object):
	'p'
	def __init__(self):
		self.name = 'liliting'
		print 'p'
	def talk(self):
		print self.name
class A(P):
	'a'
	def __init__(self):
		super(self.__class__,self).__init__()
		self.talk()
		print 'a'
	def talk(self):
		print self.name

class Time60(object):
	def __init__(self,hr,minu):
		self.hr  = hr
		self.minu = minu
	def __str__(self):
		return '%d:%d' % (self.hr,self.minu)
	__repr__ = __str__
	def __iadd__(self,other):
		self.hr +=other.hr
		self.minu+=other.minu
		return self
	def __add__(self,other):
		return self.__class__(self.hr+other.hr,self.minu+other.minu)

class RandSeq(object):
	def __init__(self,data):
		self.data = data
	def __iter__(self):
		return self
	def next(self):
		from random import choice
		return choice(self.data)

class AnyIter(object):
	def __init__(self,data,safe=False):
		self.safe = safe
		self.iter = iter(data)
	def __iter__(self):
		return self
	def next(self,howmany = 1):
		retval = []
		for eachItem in range(howmany):
			try:
				retval.append(self.iter.next())
			except StopIteration:
				if self.safe:
					break
				else:
					raise
		return retval

class NumStr(object):
	def __init__(self,n = 0, s = ''):
		self.num = n
		self.string = s
	def __str__(self):
		return '[%d :: %r]' % (self.num,self.string)
	__repr__ = __str__
	def __add__(self,other):
		if isinstance(other,self.__class__):
			return self.__class__(self.num+other.num,self.string+other.string)
		else:
			raise TypeError,'Illegal argument type or built-in operation'
	def __mul__(self,num):
		if isinstance(num,int):
			return self.__class__(self.num*num,self.string*num)
		else:
			raise TypeError,'Illegal argument type or built-in operation'
	def __nonzero__(self):
		return self.num or len(self.string)
	def __norm_cval(self,cmpres):
		return cmp(cmpres,0)
	def __cmp__(self,other):
		return self.__norm_cval(cmp(self.num,other.num))\
		 + self.__norm_cval(cmp(self.string,other.string)) 

from warnings import warn
class ReqStrSugRepr(type):
	def __init__(cls,name,bases,attrd):
		super(ReqStrSugRepr,cls).__init__(name,bases,attrd)
		if '__str__' not in attrd:
			raise TypeError('Class requires overriding of __str__()')
		if '__repr__' not in attrd:
			warn('Class suggests overriding of __repr__()\n',stacklevel = 3)
		print
		print cls
		print name
		print bases
		print attrd

class Foo(object):
	__metaclass__ = ReqStrSugRepr
	def __str__(self):
		return 'Instance of class:',self.__class__.__name__
	def __repr__(self):
		return self.__class__.__name__

class C(object):
	def __call__(self,name):
		print 'I am ' + name
	
