#!/usr/bin/env python
# -*- coding=utf-8 -*-



import time
import shelve

s 	= shelve.open('db.shelve')
try:
	db = s['user']
except (KeyError):
	db = {}


def newuser():
	prompt = 'login desired:'
	while True:
		name = raw_input(prompt)
		if db.has_key(name):
			prompt = 'name taken ,try another:'
			continue
		else:
			break

	pwd 	 	= raw_input('password:')
	db[name] 	= {'password':pwd}
	s['user'] 	= db

def olduser():
	name = raw_input('login:')
	pwd  = raw_input('password:')
	passwd = db.get(name)
	if db[name][logintime] - time.time() < 3600 * 4:
		print 'You already logged in at: ' + time.strftime('%Y-%m-%d %H:%m:%s',db[name][logintime])
	if passwd == pwd:
		print 'welcom back',name
		db[name] = {'logintime':time.time()}
	else:
		print 'login incorrect'

def listUser():
	count = len(db)
	for user in db:
		print user,db[user]['password']
	print 'count:'+str(count)

def delUser():
	name = raw_input('you will deltete user:')
	if db.has_key(name):
		del db[name]
		print 'delete success'
	else:
		print 'you delete user not exist'

def showwmenu():
	prompt = """
		(N)ew User Login
		(E)xisting User Login
		(L)ist users
		(D)elete user
		(Q)uit
		Enter choice:"""
	done = False
	while not done:
		try:
			choice = raw_input(prompt).strip()[0].lower()
		except (EOFError,KeyboardInterrupt,IndexError):
			choice = 'q'
		print '\nYou picked:[%s]' % choice
		if choice not in 'neqld':
			print 'invalid option,try again'
		else:
			done = True

	if choice == 'n':
		newuser()
	elif choice == 'e':
		olduser()
	elif choice == 'l':
		listUser()
	elif choice == 'd':
		delUser()

	s.close()
if __name__ == '__main__':
	showwmenu()