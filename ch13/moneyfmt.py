#/usr/bin/env python
# -*-coding:utf-8-*-

class MoneyFmt(object):
	def __init__(self,value=0.0,ccy='$',mark=False):#constructor
		self.__value = value
		self.__ccy 	 = ccy

	def update(self,value=None):
		if isinstance(value,(float,int)):
			self.__value = value
		else:
			raise TypeError('please input a float')

	def __repr__(self):
		return `self.__value`

	def __str__(self):
		return self.__dollarize()

	def __nonzero__(self):
		return bool(self.__value)

	def __dollarize(self):
		if isinstance(self.__value,(float,int)):
			fu = ''
			if self.__value < 0:
				fu = '-'
			f = str(abs(self.__value)).split('.')
			try:
				return fu + self.__ccy + self.__addcomma(f[0]) + '.' + f[1][:2]
			except IndexError:
				return fu + self.__ccy + self.__addcomma(f[0]) + '.00'
		else:
			raise TypeError('please input a float')

	def __addcomma(self,numStr):
		if int(numStr) < 999:
			return numStr
		length = len(numStr) % 3
		retval = numStr[:length]+','
		newstr = numStr[length:]
		for i,s in enumerate(newstr):
			if (i+1) % 3 == 0:
				retval += s+',' 
			else:
				retval += s
		return retval.strip(',')

if __name__ == '__main__':
	mymoney = MoneyFmt(45.3234)
	print mymoney
	print repr(mymoney)
	mymoney.update(44.33)
	print mymoney