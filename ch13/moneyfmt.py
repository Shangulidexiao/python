#/usr/bin/env python
# -*-coding:utf-8-*-

class MoneyFmt(object):
	def __init__(self,value=0.0):#constructor
		self.value = value
	def update(self,value=None):
		if value not None:
			self.value = value
	def __repr__(self):
		return `self.value`
	def __str__(self):
		return '$%.2f' % self.value
	def __nonzero__(self):
		return int(self.value)
	def dollarize(money):
		if isinstance(money,float):