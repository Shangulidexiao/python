#! /usr/bin/env python
# -*-coding:utf-8-*-

"练习"

from socket import *

HOST = ''
PORT = 8080
BUFSIZE = 1024
ADDR = (HOST,PORT)

s = socket(AF_INET,SOCK_STREAM)
s.bind(ADDR)
s.listen(100)

try:
	while True:
		print 'waiting for connect'
		c,addr = s.accept()
		print c.getsockname(),'is connected'
		while True:
			data = c.recv(BUFSIZE)
			if not data:
				break
			print data
			c.send('hello')
except EOFError,KeyboardInterrupt:
	s.close()




