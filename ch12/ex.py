#!/usr/bin/env python
# -*-coding:utf-8 -*-

# 12.1
搜索路径：名词：python搜索模块的路径
路径搜索：动词: python在路径中搜索路径的动作

# 12.2
 from mymodule import foo 只导入foo函数并且导入当前名字空间
 import mymodule 将mymodule全部导入必须用mymodule访问

# 12.3
import module 是导入module到当前模块
from module import * 是将module的内容导入到当前模块

# 12.4
名称空间：
变量作用域：

# 12.5
(a)  mysys = __import__('sys')
(b)  

# 12.6
def importAs(module):
	return __import__(module)

# 12.7
def 