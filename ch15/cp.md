#正则
re模块
compile(pattern,flags=0)
match(pattern,string,flags=0)
search(pattern,string,flags=0)
findall(pattern,string,flags=0)
finditer(pattern,string,flags=0)
split(pattern,stirng,max=0)
sub(pattern,repl,string,max)
group(num=0)
groups()

compile将返回regex对象
match和search返回匹配对象 主要有groups和group
groups 返回子组
group 返回所有匹配对象和子组

pi = '3\.14'

email = '([\w\.]+)@(\w+\.)*\w+\.\w+'

c = '(\w{3}abc)\1'

re.findall(c,'333abc333abc').group()