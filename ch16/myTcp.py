#!/usr/bin/env python
# -*- coding:utf-8 -*-

"tcp 客户端"

from socket import *

HOST = '10.21.77.65'
PORT = 8000
ADDR = (HOST,PORT)

client = socket(AF_INET,SOCK_STREAM)
client.connect(ADDR)
print '1.',client.getsockname()
print '2.',client.getpeername()
print client.gettimeout()
try:
	while True:
		data = raw_input('>')
		if not data:
			break
		client.send(data)
		recv = client.recv(1024)
		if not recv:
			break
		print recv
except (EOFError,KeyboardInterrupt), e:
	print e
finally:
	client.close()