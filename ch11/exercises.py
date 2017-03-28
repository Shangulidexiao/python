#!/usr/bin/env python
# -*-  coding=utf-8 -*-

"第十一章练习题"

# 11.1
def countToFour1():
	for eachNum in range(5):
		print eachNum

def countToFour2(n):
	for eachNum in range(n,5):
		print eachNum

def countToFour3(n=1):
	for eachNum in range(n,5):
		print eachNum

Input countToFour1 countToFour2 countToFour3
2		error		2,3,4			2,3,4
4		error		4					4
5		error		None			None
nothing 1,2,3,4		error			1,2,3,4

# 11.2
def addmul(a,b):
	return (a+b,a*b)

# 11.3
(a)def max2(a,b):
	if a>b: 
		return a 
	else:
		return b 
def min2(a,b):
	if a<b: 
		return a 
	else:
		return b 
(b) 
def my_max(*alist):
	max = 0
	if alist:
		for a in alist:
			if max < a:
				max = a
	return max
def my_min(*alist):
	min = 0
	if alist:
		for a in alist:
			if min > a:
				min = a
	return min

# 11.4
写一个函数把由小时和分钟表示的时间转换为只用分钟表示的时间
def mytime():
	try:
		minuates = int(raw_input('please input a minuates:'))
	except KeyboardInterrupt,e:
		print str(e)+'\nquit'
	except ValueError:
		print 'please input a number'
	else:
		m = minuates % 60
		h = (minuates - m) / 60
		print 'please you input time is %d:%d' % (h,m)

# 11.5
def tax(x=0.17):
	gprice = raw_input('please input a good price')
	return gprice * x

# 11.6
def printf(*args):
	fmt = '%s' * len(args)
	print fmt % args
# 11.7
	map(lambda x,y:(x,y),[1,2,3],[1,2,3])
	map(None,[1,2,3],[1,2,3])
	zip([1,2,3],[1,2,3])
# 11.8
def leapYear(year):
	if not isinstance(year,int):
		return 'error'
	if year % 4 == 0: 
		if year % 100 != 0:
			return True
		elif year/4 % 100 == 0:
			return True
	return False
filer(leapYear,range(2000,2017))
[year for year in range(2000,2017) if year % 4 == 0 and year % 100 != 0]

# 11.9
def average(alist):
	return reduce(lambda x,y:x+y,alist)/len(alist)

# 11.10
去掉.的所有文件

# 11.11
def file_strip(filename,newfile = None):
	if newfile == None:
		try:
			fobj = open(filename,'r')
		except IOError,e:
			return '要读取的文件不存在'
		else:
			flist = map(lambda x:x.strip()+'\n',fobj.readlines())
			fobj.close()
			try:
				wobj  = open(filename,'w')
			except IOError,e:
				return '写入文件失败，请检查权限'
			else:
				wobj.writelines(flist)
				wobj.close()
	else:
		try:
			fobj = open(filename,'r')
		except IOError,e:
			return '要读取的文件不存在'
		else:
			flist = map(lambda x:x.strip()+'\n',fobj.readlines())
			fobj.close()
			try:
				wobj  = open(newfile,'w')
			except IOError,e:
				return '写入文件失败，请检查权限'
			else:
				wobj.writelines(flist)
				wobj.close()

# 11.12

# 11.13
(a)
def mult(x,y):
	return x * y
(b)
def nmult(n):
	"计算阶乘"
	return reduce(mult,range(1,n+1))
(c)
reduce(lambda x,y:x*y,range(1,n+1))
(d)

# 11.14


