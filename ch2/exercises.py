#!/usr/bin/env python
# -*- coding=utf-8 -*-

"python 核心编程第二章习题"

# 2.1

name = 'python'
age  = 23

print 'My name is %s , age is %d' % (name,age)

# 2.2 
# (a) 用来计算 1 + 2 * 4 表达式的值
# (b) 上述脚本什么都不输出
# (c) 和我的预期一样
# (d) 代码单独执行不会有输出 在解释器中执行会输出9
# (e) 在 1 + 2 * 4 的前面加入print

# 2.3 
8 + 4
9 - 4
8 / 4
4 * 5
9 % 5
5 ** 2


# 2.4
str1 = raw_input('please input you like string:')
print str1

num = raw_input('please input a number:')
print int(num)

# 2.5

i = 0
while i <= 10:
	print i
	i += 1

for item in range(11):
	print item

# 2.6
num = int(raw_input('please input a number:'))
if num > 0:
	print '正数'
elif num == 0:
	print '等于0'
else:
	print '负数'

# 2.7
str2 = raw_input('please input a string:\n')
str2Len = len(str2)
i = 0
while i < str2Len:
	print str2[i]
	i += 1

for s in range(str2Len):
	print str2[s]

# 2.8
# 自定义列表
list1 = [1,2,3,4,5]
print sum(list1)

# for循环列表
list2 = []
for i in range(5):
	num = int(raw_input('please input a number:'))
	list2.append(num)
print sum(list2)

# while循环列表
list3 = []
i = 0
while i < 5:
	num = int(raw_input('please input a number:'))
	list3.append(num)
	i += 1
print sum(list3)

# 2.9 

flist = [2,3,4,5,7]
print float(sum(flist))/len(flist)

# 2.10

while True:
	num = int(raw_input('Please input a 0~100 number:\n'))
	if 0 <= num <= 100:
		print 'ok'
		break
	else:
		print 'you input is error'