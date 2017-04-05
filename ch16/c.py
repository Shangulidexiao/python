#! /usr/bin/env python
# -*-coding:utf-8-*-

from socket import *

HOST = 'localhost'#表示可以绑定在所有的地址上
PORT = 8080
BUFSIZ = 1024
ADDR = (HOST,PORT)

c = socket(AF_INET,SOCK_STREAM)
c.connect(ADDR)

try:
	while True:
		data = raw_input('>')
		if not data:
			break
		c.send(data)
		print c.recv(BUFSIZ)
except EOFError,KeyboardInterrupt:
	c.close()