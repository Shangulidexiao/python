#! /usr/bin/env python
# -*-coding:utf-8

#15.1
bt = '[hb][aiu]t'

#15.2
name = r'\w+\s\b\w+'

#15.3
first = r'\w+[\s|,]\w+'

#15.4
var = r'[a-zA-Z_][\w_]*'

#15.5
rex = r'\d+\s([a-zA-Z]+\s)+[a-zA-Z]+'

#15.6
wwwRe = r'www\.\w+\.(com|edu|net)'

#15.7
numRe = r'\d+'

#15.8
longRe = r'\d+[Ll]'

#15.9
floatRe = r'\d+\.\d+'

#15.10
complexRe = r'(\d+\.\d+\+)*(\d+\.\d+)*j'

#15.11
email = '([\w\.]+)@(\w+\.)*\w+\.\w+'

#15.12
urlRe = r'((http|https)://)*([\w]+\.)*[\w]+(\.[\w]+)+'
re.match(urlRe,'xgo.cn').group()

# 15.13
typeRe = r'<type\s\'(\w+)\'>'
typeRe = r"<type\s'(\w+)'>"
re.match(typeRe,"<type 'int'>").groups()

# 15.14
monthRe = r'(^0?[1-9]$)|(^1[0-2]$)'
re.match(monthRe,"12").group()

#15.15
cardRe = r'(^\d{4}-\d{6}-\d{5}$)|(^\d{4}(-\d{4}){3}$)'
re.match(cardRe,"4352-6675-3333-6344").group()

#15.19

#15.28
phoneRe = r'((\d{3}-)|(\(\d{3}\)\s))*\d{3}-\d{4}'
re.match(phoneRe,"800-555-1212").group()
re.match(phoneRe,"555-1212").group()
re.match(phoneRe,"(800) 555-1212").group()

#15.29


