#!/usr/bin/env python
# -*- coding:utf-8-*-

from random import randint,choice
from string import lowercase
from sys import maxint
from time import ctime

doms = ('com','edu','net','org','gov')
redata = ''
for i in range(randint(5,10)):
	dtint = randint(0,4294967296-1) #pickk date
	dtstr = ctime(dtint)
	shorter = randint(4,7)#login shorter
	em = ''
	for j in range(shorter):
		em += choice(lowercase)
	longer = randint(shorter,12)
	dn = ''
	for  j in range(longer):
		dn += choice(lowercase)
	redata += '%s::%s@%s.%s::%d-%d-%d\n' % (dtstr,em,dn,choice(doms),dtint,shorter,longer)

try:
	fobj = open('redata.txt','w')
except IOError,e:
	print 'pelase check premission'
else:
	fobj.writelines(redata)
	fobj.close()