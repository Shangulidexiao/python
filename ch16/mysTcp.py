#!/usr/bin/env python
# -*- coding:utf-8 -*-

"tcp 客户端"

from socket import *

HOST = ''
PORT = 8000
ADDR = (HOST,PORT)

server = socket(AF_INET,SOCK_STREAM)
server.bind(ADDR)
server.listen(5)

try:
	while True:
		print 'wait for connection'

		client,addr = server.accept()
		print 'connect at ' ,addr
		while True:
			recv = client.recv(1024)
			print recv
			if not recv:
				client.close()
				break
			client.send(recv+'--')
		
except (EOFError,KeyboardInterrupt), e:
	print e
finally:
	server.close()