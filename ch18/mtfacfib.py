#! /usr/bin/env python
# -*-coding:utf-8

'斐波那契|阶乘|累加和'

from myThread import MyThread
from time import ctime,sleep

def fib(x):
	sleep(0.005)
	if x < 2:
		return 1
	return (fib(x-2)+fib(x-1))

def fac(x):
	sleep(0.1)
	if x < 2:
		return 1
	return (x * fac(x-1))

def sumz(x):
	sleep(0.1)
	if x < 2:
		return 1
	return (x + sumz(x-1))

funcs = [fib,fac,sumz]
n = 12

def main():
	nfunc = range(len(funcs))
	print '*** SINGLE THREAD'
	for i in nfunc:
		print 'starting ',funcs[i].__name__,'at:',ctime()
		print funcs[i](n)
		print funcs[i].__name__,'finished at:',ctime()
	print '\n*** MULTIPLE THREADS'
	threads = []
	for i in nfunc:
		threads.append(MyThread(funcs[i],(n,),funcs[i].__name__))
	for i in nfunc:
		threads[i].start()
	for i in nfunc:
		threads[i].join()	
		print threads[i].getResult()
	print 'all Done!!'
if __name__ == '__main__':
	main()