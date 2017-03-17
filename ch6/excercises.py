#!/usr/bin/env python
# -*- coding=utf-8 -*-

"python 核心编程第六章习题"

# 6.1
string.index('hhhhjj','jj')
string.find('hhhhjj','jj')

# 6.2
"检测是否是合法的变量名"

import string
from keyword import kwlist

alphas = string.letters + '_'
nums   = string.digits

print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long.'
inp = raw_input('Identifier to test? ')

inplength = len(inp)

if (inplength == 1) and (inp in alphas):
	print 'ok'
else:
	print 'invalid: first symbol must be 16  alphabetic'

if inplength > 1:
	if inp[0] not in alphas:
		print '''invalid: first symbol must be 16  alphabetic'''
	else:
		alphnums = alphas + nums
		for otherChar in inp[1:]:
			if otherChar not in alphnums:
				print '''invalid: remaining 22  symbols must be alphanumeric'''
				break
		else:
			if inp in kwlist:
				print 'ok'
			else:
				print 'invalid:you input is a keyword' 

# 6.3
(a) 

num = raw_input('输入一串数字用空格分割')
strlist = num.split(' ')
numlist = []
for i in strlist:
	numlist.append(int(i))
numlist.sort()
numlist.reverse()

strlist.sort()
strlist.reverse()

#6.4

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

def testGrade():
	grades = []
	while True:
		num = raw_input('请输入学生的分数，结束请输入 ! ')
		if num == '!':
			break
		try:
			num = int(num)
		except ValueError,e:
			print str(e)
		else:
			grades.append(num)
			print grade(num)
			print sum(grades)/len(grades)

# 6.5
(a)
str2 = raw_input('please input a string:\n')
str2Len = len(str2)
i = 0
while i < str2Len:
	print str2[i]
	print str2[str2Len-i-1]
	i += 1

for s in range(str2Len):
	print str2[s]
	print str2[str2Len-s-1]

(b)
str1 = 'abc'
str2 = 'abc'
def cmpi(str1,str2):
	if len(str1) != len(str2):
		return -1
	for i in range(len(str1)):
		if str1[i] != str2[i]:
			return -1
	return 0
# 6.6

def strip(str1):
	whiteSpace = ' 		'
	strLen  = len(str1) - 1
	i 		= 0
	start 	= 0
	end 	= strLen
	while True:
		if (str1[i] not in whiteSpace) and ((str1[strLen-i] not in whiteSpace)):
			break
		if  str1[i] in whiteSpace:
			start += 1
		if  str1[strLen-i] in whiteSpace:
			end -= 1
		i += 1
		if i > strLen/2:
			break
	if end == strLen:
		end = None
	return str1[start:end]
# 6.7
#!/usr/bin/env python

#输入一个数
num_str = raw_input('Enter a number')

# 转化成整型
num_num = int(num_str)

#生成1-num_num 以1为等差的列表
fac_list = range(1, num_num+1)
print "BEFORE:", fac_list

# i赋值为0
i = 0

# fac_list 循环 error索引超出访问范围
while i < len(fac_list):
	# 能被
	if num_num % fac_list[i] == 0:
		del fac_list[i]

	# 循环变量加1
	i = i + 1

# 输出列表
print "AFTER:", fac_list
# 6.8
def turnNum(num):
	numstr 		= ['zero','one','two','three','four','five','six','eleven','eight','nine']
	inputNum 	= []
	tempNum 	= num
	if not isinstance(num,int):
		return '请输入0-1000的数字'
	if 0 < num < 1000:
		if num / 1000 >= 1:
			inputNum.append(numstr[num / 1000])
			tempNum -= num / 1000 * 1000
		if tempNum / 100 >= 1:
			inputNum.append(numstr[tempNum / 100])
			tempNum -= tempNum / 100 * 100
		if tempNum / 10 >= 1:
			inputNum.append(numstr[tempNum / 10])
			tempNum -= tempNum / 10 * 10
		inputNum.append(numstr[tempNum])
		return '-'.join(inputNum)
	else:
		return '请输入0-1000的数字'

# 6.9
def toHour(minute):
	hour = minute/60
	minu = minute - (hour * 60)
	return str(hour)+':'+str(minu).rjust(2,'0')

# 6.10

def reveredChar(str1):
	from string import letters
	str2 = ''
	for chr1 in str1:
		if chr1 in letters:
			if chr1.islower():
				str2 += chr1.upper()
			else:
				str2 += chr1.lower()
		else:
			str2 += chr1
	return str2

# 6.11

def intToIp(num):
	hexs = hex(num)[2:].rjust(8,'0')
	fhex = range(0,8,2)
	ips  = []
	for ip in fhex:
		ips.append(str(int('0x'+hexs[ip:ip+2],16)))
	return '.'.join(ips)

def ipToint(ip):
	ints = ip.split('.')
	hexs = ''
	for int1 in ints:
		hexs += hex(int(int1))[2:]
	return int('0x'+hexs,16)

# 6.12

def findchar(string,char):
	strlen = len(string)
	i = 0
	while i < strlen:
		if string[i] == char:
			return i
		i += 1
	return -1
def rfindchar(string,char):
	i = len(string)-1
	while i >= 0:
		if string[i] == char:
			return i
		i -= 1
	return -1
def subchar(string,origchar,newchar):
	strlen = len(string)
	i = 0
	while i < strlen:
		if string[i] == origchar:
			return string[None:i] + newchar + string[i+1:]
		i += 1
	return -1

# 6.13
def atoc(string):
	if 'j' not in string:
		return complex(float(string))
	com = string.split('+')
	if len(com) == 2:
		return complex(float(com[0]),float(com[1][:len(com[1])-1]))
	else:
		return complex(0,float(string[:len(string)-1]))

# 6.14
from random import randint
def Rochambeau():
	content = ['1','2','3']
	while True:
		client = raw_input("""
			剪刀石头布游戏\n
			剪刀输入１\n
			石头输入２\n
			布输入３\n
			""")
		if client in content:
			break
	keyword = ['剪刀','石头','布']
	win = ['13','21','32']
	lose = ['12','23','31']
	ser = randint(0,2)
	ifstr = content[ser]+client
	print ifstr
	print '你出' + keyword[int(client)-1]
	print '我出' + keyword[ser]
	if ifstr in win:
		print '我赢了'
	elif ifstr in lose:
		print '你赢了'
	else:
		print '平手'
# 6.15
strtime = raw_input('请输入')
structTime = strptime(strtime)


# 6.17
def myPop(list1):
	listLen = len(list1)
	last 	= list1[listLen-1]
	del list1[listLen-1]
	return last

# 6.19
多列输出.有任意项的序列或者其他容器,把它们等距离分列显示.由调用者提供数据和
输出格式.例如,如果你传入 100 个项并定义 3 列输出,按照需要的模式显示这些数据.这种情况下,应
该是两列显示 33 个项,最后一列显示 34 个.你可以让用户来选择水平排序或者垂直排序.

def cutContent(list1,col,rh = 0):
	# 构建列表
	listLen = len(list1)
	bu 		= 0
	if rh == 0 and listLen % col != 0 and col < listLen:
		yu 		= listLen % col
		bu 		= col - yu
		start 	= listLen - yu
		for i in xrange(bu):
			list1.insert(start + i,' ')
	else:
		pass
	# 输出列表
	i 		= 0
	nLen 	= listLen + bu
	while i < nLen :
		if (i+1) % col == 0:
			print list1[i]
		else:
			print str(list1[i])+'\t',
		i += 1
