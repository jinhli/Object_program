#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 6/4/18

#储备知识 exec
#参数1：字符串形式的命令
#参数2：全局作用， 默认使用globals()
#参数3：局部作用域, 默认使用locals()

g={
'x':1,
'y':2
}
l={}

exec('''
global x,z
x=100
z=200

m=300
''',g,l)

print(g)

