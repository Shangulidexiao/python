#! /usr/bin/env python
# -*-coding:utf-8-*-

from socket import *

HOST = 'localhost'#表示可以绑定在所有的地址上
PORT = 2000
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_NET,SOCK_STREAM)
tcpCliSock.connent(ADDR)

while True:
	data = raw_input('>')
	if not data:
		break
	tcpCliSock.send(data)
	data = tcpCliSock.recv(BUFSIZ)
	if not data:
		break
	print data

tcpCliSock.close()