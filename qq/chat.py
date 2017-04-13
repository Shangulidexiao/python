#! /usr/bin/env python
# -*- coding:utf-8 -*-

"聊天软件"

import sys
from PyQt4 import QtGui,QtCore
 
class Chat(QtGui.QMainWindow):
	"聊天软件入口类"
	def __init__(self):
		super(self.__class__,self).__init__()
		self.initUI()

	def initUI(self):
		QtGui.QToolTip.setFont(QtGui.QFont('SansSerif',10))

		self.showMenu()#菜单栏
		self.statusBar().showMessage('Ready') #状态栏

		self.resize(300,500)
		self.center()
		self.setWindowTitle('Chat')
		self.setWindowIcon(QtGui.QIcon('res/img/logo.svg'))
		self.show()

	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def showMenu(self):
		exitAction = QtGui.QAction(QtGui.QIcon('res/img/exit.png'),'&Exit',self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit application')
		exitAction.triggered.connect(QtCore.QCoreApplication.instance().quit)

		menubar = self.menuBar()
		fileMenu = menubar.addMenu(u'&文件')
		fileMenu.addAction(exitAction)

		self.toolbar = self.addToolBar('Exit')
		self.toolbar.addAction(exitAction)

	def showButton(self,qwidget):
		okBtn = QtGui.QPushButton('ok',qwidget)
		cancel = QtGui.QPushButton('cancel',qwidget)
		hbox = QtGui.QHBoxLayout()
		hbox.addStretch(1)
		hbox.addWidget(okBtn)
		hbox.addWidget(cancel)
		vbox = QtGui.QVBoxLayout()
		vbox.addStretch(1)
		vbox.addLayout(hbox)
		qwidget.setLayout(vbox)

		grid = QtGui.QGridLayout()
		self.setLayout(grid)
		grid.addWidget(button,())

	def closeEvent(self,event):
		reply = QtGui.QMessageBox.question(self,'Message','Are you sure to quit?',
			QtGui.QMessageBox.Yes|QtGui.QMessageBox.No,QtGui.QMessageBox.No)
		if reply == QtGui.QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()
def main():
	app = QtGui.QApplication(sys.argv)
	chat = Chat()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()