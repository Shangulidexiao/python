#! /usr/bin/env python
# -*-coding:utf-8 -*-

import sys
from PyQt4 import QtGui,QtCore

class Test(QtGui.QWidget):
	def __init__(self):
		super(self.__class__,self).__init__()
		#self.initUI()
		self.cc()

	def initUI(self):
		grid = QtGui.QGridLayout()
		self.setLayout(grid)
		names = ['cls','back','','close','7','8','9','/','4','5','6','*','1','2','3','-','0','.','=','+']
		positions = [(i,j) for i in range(5) for j in range(4)]

		for positon,name in zip(positions,names):
			if name == '':
				continue
			button = QtGui.QPushButton(name)
			grid.addWidget(button,*positon)

		self.move(300,150)
		self.setWindowTitle('calculator')
		self.show()
	def cc(self):
		lcd = QtGui.QLCDNumber(self)
		sld  = QtGui.QSlider(QtCore.Qt.Horizontal,self)

		vbox = QtGui.QVBoxLayout()
		vbox.addWidget(lcd)
		vbox.addWidget(sld)

		self.setLayout(vbox)
		sld.valueChanged.connect(lcd.display)
		self.move(300,150)
		self.setWindowTitle('calculator')
		self.show()
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Test()
    sys.exit(app.exec_())