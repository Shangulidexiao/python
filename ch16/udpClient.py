#! /usr/bin/env python
# -*-coding:utf-8-*-

from socket import *

HOST = 'localhost'#表示可以绑定在所有的地址上
PORT = 2000
BUFSIZ = 1024
ADDR = (HOST,PORT)

udpSerSock = socket(AF_INET,SOCK_DGRAM)

try:
	while True:
		data = raw_input('>')
		if not data:
			break
		udpSerSock.sendto(data,ADDR)
		data,ADDR = udpSerSock.recvfrom(BUFSIZ)
		if not data:
			break
		print data
except EOFError,KeyboardInterrupt:
	udpSerSock.close()