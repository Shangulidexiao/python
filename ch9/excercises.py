#!/usr/bin/env python
# -*- coding=utf-8 -*-

# 9.1

def source():
	fobj  = None
	while fobj == None:
		fname = raw_input('请输入一个文件名：')
		try:
			fobj = open(fname)
		except IOError,e:
			print str(e) + '请重新输入文件名'
	for line in fobj:
		if '#' not in line.strip():
			print line
			continue
		if  line.strip().startswith('#'):
			continue
		index =	line.strip().find('#')
		if  index != -1:  
			print line[:index]
	fobj.close()
# 9.2
def showN():
	fobj,n,i = None,None,1
	while fobj == None or n == None:
		if n == None:
			try:
				n = int(raw_input('请输入你要读取的行数'))
			except ValueError,e:
				print str(e)
				continue
		if fobj == None:
			fname = raw_input('请输入一个文件名：')
			try:
				fobj = open(fname)
			except IOError,e:
				print str(e)
	for line in fobj:
		print line,
		if i > n:
			break
		i += 1
	fobj.close()

# 9.3
def linenum(filename):
	num , fobj= 0 , None
	try:
		fobj = open(filename)
	except IOError,e:
		return False
	for line in fobj:
		num += 1
	fobj.close()
	return num

# 9.4 page('excercises.py')
def page(filename):
	num , fobj= 1 , None
	try:
		fobj = open(filename)
	except IOError,e:
		print str(e)
	for line in fobj:
		print str(num) + line
		if num % 25 == 0:
			go = raw_input('按回车键继续')

		num += 1
	fobj.close()

# 9.5
def getgrage():


# 9.6 diff('excercises.py','excercises.py')
def diff(file1,file2):
	fobj  = safe_open(file1)
	fobj1 = safe_open(file2)
	if fobj == False or fobj1 == False:
		return False
	flist  = fobj.readlines()
	flist1 = fobj1.readlines()
	fobj.close()
	fobj1.close()
	num    = min(len(flist),len(flist1))
	i = 0
	while i < num:
		if flist[i] != flist1[i]:
			return i + 1
		i += 1
	return False


def safe_open(filename,mode='r'):
	fobj = False
	try:
		fobj = open(filename,mode)
		return fobj
	except IOError,e:
		return fobj

	
# 9.8 
modename = raw_input('请输入一个模块名')
__import__(modename)
print dir(modename)

# 9.13
import sys
print sys.argv

# 9.14

# 9.15
def copy(file1,file2):
	fobj = safe_open(file1)
	fobj1 = safe_open(file2,'w')
	if fobj == False or fobj1 == False:
		return False
	for line in fobj:
		fobj1.write(line)
	fobj.close()
	fobj1.close()

# 9.16
# 首先遍历每个文件 然后每行要拆分成n个80个字符
def line80(str1):
	newstr,srcstr = '',str1
	if len(str1) <= 80:
		return str1
	while len(srcstr) > 80:


