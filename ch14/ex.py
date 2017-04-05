#! /usr/bin/env python
# -*-coding:utf-8-*-

import os
ret = os.fork()
if ret == 0:
	print 'son'
else:
	print 'parent'