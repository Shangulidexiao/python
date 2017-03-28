# 可调用对象
函数、方法、类、实现__call__方法的类实例

#### 代码对象
1. callable 判断函数是否可调用
2. compile 第一个参数 要编译的代码 第二个参数 存放代码对象的文件名字 第三个参数 eval 可求值得表达式 exec 单一可执行语句组 single 单一可执行语句 
3. 导入模块会执行顶层代码 if __name__ == '__main__'
4. execfile(filename,globals,locals) 执行一个文件
5. 

## 执行二进制程序
1. os.system()


ret = os.fork()
if ret == 0:
	print 'hanjian'
else:
	print 'liliting'