#! /usr/bin/env python
# -*- coding:utf-8 -*-

"生产者和消费者"

from random import randint
from time import sleep
from Queue import Queue
from myThread import MyThread

def writeQ(queue):
	print 'producing obect for Q...'
	queue.put('xxx')
	print 'size now ',queue.qsize()

def readQ(queue):
	val = queue.get()
	print 'consumed object from Q... size now',queue.qsize()
	return val

def writer(queue,loops):
	for i in range(loops):
		writeQ(queue)
		sleep(randint(1,3))

def reader(queue,loops):
	for i in range(loops):
		print readQ(queue)
		sleep(randint(2,5))

funcs = [writer,reader]
nfuncs = range(len(funcs))

def main():
	nloops = randint(4,5)
	q = Queue(32)

	threads = []
	for i in nfuncs:
		threads.append(MyThread(funcs[i],(q,nloops),funcs[i].__name__))

	for i in nfuncs:
		threads[i].start()

	for i in nfuncs:
		threads[i].join()
	print 'all done!'

if __name__ == '__main__':
	main()