#! /usr/bin/env python
# -*-coding:utf-8-*-

'socket test'
from socket import *
from time import ctime

HOST = ''#表示可以绑定在所有的地址上
PORT = 2000
BUFSIZ = 1024
ADDR = (HOST,PORT)


tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)#5 表示最多允许5个连接

try:
	while True:
		print 'waiting for connection'
		tcpCliSock,addr = tcpSerSock.accept()
		print '... connected form:',addr

		while True:
			data = tcpCliSock.recv(BUFSIZ)
			print 'this client send is' + data
			if not data:
				break
			tcpCliSock.send('[%s] %s' % (ctime(),data))
except EOFError,KeyboardInterrupt:
	tcpCliSock.close()
	tcpSerSock.close()
