#!/usr/bin/env python
# -*- coding:utf-8 -*-

"13章练习题"

# 13.1


# 13.2
方法是在类内定义的函数，只能由实例调用

# 13.3
def dollarize(money):
	if isinstance(money,float):
		fu = ''
		if money < 0:
			fu = '-'
		f = str(round(abs(money),2)).split('.')

