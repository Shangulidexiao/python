#! /usr/bin/env python

from time import sleep,ctime

def loop0():
	print 'start loop 0 at: ',ctime()
	sleep(4)
	print 'loop 0 done at:',ctime()

def loop1():
	print 'start loop 2 at: ',ctime()
	sleep(2)
	print 'loop 2 done at:',ctime()

def main():
	 print 'starting at;',ctime()
	 loop0()
	 loop1()
	 print 'all done at:',ctime()

def tmain():
	print 'strating at:',ctime()
	thread.start_new_thread(loop0,())
	thread.start_new_thread(loop1,())
	#sleep(6)
	print 'all Done at:',ctime()
if __name__ == '__main__':
	main()