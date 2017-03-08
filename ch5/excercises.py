#!/usr/bin/env python
# -*- coding=utf-8 -*-

"python 核心编程第五章习题"

# 5.1
标准整数类型是最通用的数字类型
Python 的长整数类型能表达的 数值仅仅与你的机器支持的(虚拟)内存大小有关

def mutli(oneNum,twoNum):
	"计算两个数的乘积"
	isNumber = (int,float,long,complex)
	if isinstance(oneNum,isNumber) and isinstance(twoNum,isNumber):
		return oneNum * twoNum
	return False;

multi(3,5)

# 5.3

def grade(fraction):
	""" 根据分数然会对应的等级 """
	if 90 <= fraction <= 100:
		return 'A'
	elif 80 <= fraction < 90:
		return 'B'
	elif 70 <= fraction < 80:
		return 'C'
	elif 60 <= fraction < 70:
		return 'D'
	elif 0 <= fraction < 60:
		return 'F'
	else :
		return ''

# 5.4

def leapYear(year):
	if not isinstance(year,int):
		return 'error'
	if year % 4 == 0: 
		if year % 100 != 0:
			return True
		elif year/4 % 100 == 0:
			return True
	
	return False
# 5.5
def giveChange(money):
	cents = (25,10,5,1)
	numCents = {}
	if not isinstance(money,float):
		return 'error'
	tmp = money*100
	for cent in cents:
		num = int(tmp / cent)
		tmp = tmp - num * cent
		numCents[cent] = num
	return numCents	

# 5.6
ex = raw_input('Please input a expreass:\n')

if len(ex.split('+')) == 2:
	nums = ex.split('+')
	print float(nums[0]) + float(nums[1])
elif len(ex.split('-')) == 2:
	nums = ex.split('-')
	print float(nums[0]) - float(nums[1])
elif len(ex.split('*')) == 2:
	nums = ex.split('*')
	print float(nums[0]) - float(nums[1])
elif len(ex.split('/')) == 2:
	nums = ex.split('/')
	print float(nums[0]) / float(nums[1])
elif len(ex.split('%')) == 2:
	nums = ex.split('%')
	print float(nums[0]) - float(nums[1])
elif len(ex.split('**')) == 2:
	nums = ex.split('**')
	print float(nums[0]) - float(nums[1])

# 5.7

price  = 500 * 0.17

# 5.8

def square(width,height):
	return width * height

def cube(width,height,length):
	return width * height * length

from math import pi

def circular(r):
	return pi * r ** 2

def ball(r):
	return 4/3 * pi * r ** 3
# 5.9
 17 + 32  = 49 两个十进制的加法
 017 + 32 = 15 + 32 = 45 017为８进制
 017 + 032 = 15 + 26 = 41 017 和032都为８进制
 56l + 78l = 124L  56 78后面都有ｌ代表长整型

# 5.15
def bigDiv(num1,num2):
	"两个数的最大公约数-中国的算法"
	# 如果相等这个数就是最大公约数
	if num1 == num2:
		return num1

	retval = 1;
	while True:
		if num1 % 2 != 0 or num2 % 2 != 0:
			break
		else:
			retval *= 2
			num1,num2 = num1/2,num2/2

	while True:
		if num1 > num2:
			result = num1 - num2
			if result == num2:
				return num2 * retval
			num1 = result
		else:
			result = num2 - num1
			if result == num1:
				return num1 * retval
			num2 = result
	return retval

# 5.17
import random
N = random.randint(2,100)
randlist = random.sample(xrange(2**31- 1) ,N)
randlist.sort()
print randlist