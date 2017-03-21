#!/usr/bin/env python

# 8.1
# statement A
if x > 0:
	# statement B
	pass
elif x < 0:
	# statement C
	pass
else:
	# statement D
	pass
	# statement E
(a) A C
(b) A D E
(c) A B
# 8.2
def myrange(f,t,i):
	"自己写的range函数"
	while f <= t:
		print f
		f +=  i
# 8.3
(a) range(0,10)
(b) range(3,19,3)
(c) range(-20,861,220)

# 8.4

def isprime(num):
	count = num / 2
	isprime = True
	while count > 1:
		if num % count == 0:
			isprime = False
			break
		count -= 1
	return isprime

# 8.5 
def getfactors(num):
	fac = [1,num]
	count = num / 2
	while count > 1:
		if num % count == 0:
			fac.append(count)
		count -= 1
	return fac
# 8.6
def primefactor(num):
	factors = getfactors(num)
	pfactors = []
	for f in factors:
		if isprime(f):
			pfactors.append(f)
	return pfactors

# 8.7
def isperfect(num):
	facs = getfactors(num)
	facs.remove(num)
	if num == sum(facs):
		return 1
	else:
		return 0

# 8.8
def nn(n):
	i 	= 1
	sum1 = 1
	while i <= n:
		sum1 *= i
		i += 1
	return sum1

# 8.9
def fibonacci(num):
	if num == 0:
		return 0
	if num == 1:
		return 1
	else:
		return fibonacci(num-1)+ fibonacci(num-2)

# 8.10
def wordnum(string):
	wordnum = len(string.split())
	yuan,fu  = 0,0
	for s in string:
		if s.lower() in 'aeiou':
			yuan += 1
		else:
			from string import letters
			if ss in letters:
				fu += 1
	return wordnum,yuan,fu		

# 8.11
def addName():
	error = 0
	names = []
	print 'input ! quit,name format is Lase name,First Name'
	while True:
		name = raw_input('please input name :')
		if name == '!':
			break
		if len(name.split(',')) ==  2:
			names.append(name)
		else:
			error += 1
	return names 

# 8.12

# 8.13
alist = ['xx' ]