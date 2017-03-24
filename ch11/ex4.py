#!/usr/bin/env python
# -*-coding=utf-8 -*-

'test'

def testit(func,*nkwargs,**kwargs):
	try:
		retval = func(*nkwargs,**kwargs)
		result = (True,retval)
	except Exception,diag:
		result = (Flase,str(diag))

	return result

def test():
	func = (int, long, float)
	vals = (1234,12.34,'1234','12.34')
	for eachFunc in funcs:
		print '-'*20
		for eachVal in vals:
			retval = testit(eachFunc,eachVal)
			if retval[0]: