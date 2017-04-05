#! /usr/bin/env python
# -*-coding:utf-8-*-

'socket test'
from socket import *
from time import ctime

HOST = ''#表示可以绑定在所有的地址上
PORT = 2000
BUFSIZ = 1024
ADDR = (HOST,PORT)


udpSerSock = socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)

try:
	while True:
		print 'waiting for message'
		data,addr = udpSerSock.recvfrom(BUFSIZ)
		udpSerSock.sendto('[%s] %s' % (ctime(),data),addr)
		print '... received from and returned to:',addr
except EOFError,KeyboardInterrupt:
	udpSerSock.close()
