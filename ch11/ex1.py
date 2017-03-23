#!/usr/bin/env python
# -*-coding=utf-8-*-

"函数定义顺序问题"
def foo():
	bar()

def bar():
	print 'bar'

foo()