cxn = MySQLdb.connect(user='root',passwd='root',db='hei_admin')
连接的方法
close()
commit()
rollback()
cursor() 
errorhandler()

游标对象的属性
arraysize fechmany 一次取出多少条记录
connection
description 返回游标的活动状态
lastrowid  最后更新的id
rowcount 最后一次execute影响的行数
callproc 调用一个存储过程
close 关闭游标对象
execute 执行一个数据库命令或者查询
executemany

fetchone 得到结果集的下一行
fetchmany 得到结果集的下几行
fetchall 的到剩下的所有行
__iter__ 创建一个迭代对象
messges
next 下一行
nextset 下一个结果集
rownumber 当前结果集的索引
setinput