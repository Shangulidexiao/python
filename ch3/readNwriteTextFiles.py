#!/usr/bin/env Python

def writeFile():
	# get filename
	while True:
		fname = raw_input('Please you input a fileName:\n')
		if os.path.exists(fname):
			print "ERROR: '%s' already exists" % fname
		else:
			break
	# get file content (text) lines
	all = []
	print "\nEnter lines ('.' by itself to quit).\n"
	# loop until user terminates input
	while True:
		entry = raw_input('> ')
		if entry == '.':
			break
		else:
			all.append(entry)

	# write lines to file with proper line-ending
	fobj = open(fname, 'w')
	fobj.writelines(['%s%s' % (x, ls) for x in all])
	fobj.close()
	print 'DONE!'

def readFile():
	# get filename
	fname = raw_input('Enter filename: ')
	print

	# attempt to open file for reading
	try:
		fobj = open(fname, 'r')
	except IOError, e:
		print "*** file open error:", e
	else:
	# display contents to the screen
		for eachLine in fobj:
			print eachLine,
	fobj.close()

def editFile():
	# get filename
	fname = raw_input('Enter filename: ')
	print
	# attempt to open file for reading
	try:
		fobj1 = open(fname, 'r+')
	except IOError, e:
		print "*** file open error or file is not exist:", e
	else:
		# display contents to the screen
		lines = fobj1.readlines()
		for lineNum,line in enumerate(lines):
			print str(lineNum+1) +' '+ line.strip()
		
		num = int(raw_input('please input you change number\n')) -1
		str1 = raw_input('please input you new string\n')
		confirm = raw_input('confirm chage input y no input n\n')
		if confirm == 'y':
			lines[num] = str1
			fobj1.writelines(lines)
		fobj1.close()

rw = raw_input('read file input 1 create file input 2 edit file input 3\n')

if rw == '1':
	readFile()
elif rw == '2':
	writeFile()
elif rw == '3':
	editFile()