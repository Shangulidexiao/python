#!/usr/bin/env python
# -*- coding=utf-8 -*-

"python 核心编程第七章习题"

# 7.1
update

#7.2
可以的对象 int float bool str long complex tuple forzenset
不可以的 set list dict 
可以hash的才能做字典的键

#7.3
adict = ['a':1,'b':2,'c':3]
alist = adict.keys()
alist.sort()

for i,key in enumerate(alist):
	print key,adict[key]

# 7.4
alist = [1,2,3]
blist = ['a','b','c']
dict(zip(alist,blist))

# 7.5


# 7.7
def reverse(dict1):
	newdict = {}
	if isinstance(dict1,dict):
		return False
	for key in dict1:
		newdict[dict1[key]] = key
	return newdict

# 7.8
def staff():
	print '输入q退出'
	staff = {}
	while True:
		name = raw_input('Please input name or q quit:')
		if name == 'q':
			break
		code = raw_input('Please input code:')
		if staff.has_key(code):
			print '编码已存在，本次录入失败'
		staff[code] = name
	codes = staff.keys()
	codes.sort()
	for code in codes:
		print code , staff[code]
# 这道题没有写完

# 7.9
(a) 
def tr(srcstr,dststr,string,ul=True):
	srcLen = len(string),len(srcstr)
	strLen = len(string) - srcLen
	newstr = ''
	i = 0
	if ul:
		if srcstr not in string:
			return string
		while i < strLen:
			if srcstr == string[i:i+srcLen]
			newstr = string[:i] + dststr + string[:]
			i += srcLen
	else:
		src,dst,str1 = srcstr.lower(),dststr.lower(),string.lower
		if src not in str1:
			return string
		while i < strLen:
			if srcstr == string[i:i+srcLen]
			newstr = string[:i] + dststr + string[:]
			i += srcLen		
	


# 7.10
def rot13(str1):
	from string import letters
	newstr = ''
	strlen = len(str1)
	for s in xrange(strlen):
		if str1[s] not in letters:
			newstr += str1[s]
		else:
			rindex = ord(str1[s]) + 13
			if str1[s].islower() and rindex > 122:
				rindex = 97 + rindex - 123
			elif str1[s].isupper() and rindex > 90:
					rindex = 65 + rindex - 91
			newstr += chr(rindex)
	return newstr

def rot13n(str1):
	from string import letters
	newstr = ''
	strlen = len(str1)
	for s in xrange(strlen):
		if str1[s] not in letters:
			newstr += str1[s]
		else:
			rindex = ord(str1[s]) - 13
			print rindex
			if str1[s].islower() and rindex < 97:
				rindex = 123 - 97 + rindex
			elif str1[s].isupper() and rindex < 65:
					rindex = 91 - 65 + rindex
					print rindex
			newstr += chr(rindex)
	return newstr


