#!/usr/bin/env python
# -*- coding=utf-8 -*-

"python 核心编程第四章习题"

# 4.1
身份 唯一一个标示对象的值 比如：人的身份证号
类型 这个对象是什么类型的 可以进行什么操作 比如： 男人 女人
值 对象表示的数据项 比如：就是实实在在的人 
具体定义书中有

# 4.2
不可变 int long float bool complex tuple frozenset  对象一旦创建了他的值就不能改变了，只能通过新建一个对象
可变 list set  dict 对象中的值可以改变

# 4.3
顺序访问：list tuple str 按照数据的索引来访问
映射访问：dict 数据通过一个唯一的键来访问

# 4.4 
返回python对象的类型
返回的是类型对象

# 4.5
str()函数得到的字符串可读性好， 而 repr()函数得到的字符
串通常可以用来重新获得该对象, 通常情况下 obj == eval(repr(obj)) 这个等式是成立的。
repr 等价于 ``

# 4.6
“==”比较的是值，is比较的是对象。因为每个对象只可能有一种类型的值，所以可以直接比较他们的ID，而不用先计算值再做比较。 
函数isinstance()用来确定这个对象是否属于这个类型，或者实例是否属于某个类。

# 4.8
相同点：都是顺序访问
不同点：列表的值可以改变 元组不行

# 4.9
True
True
False

