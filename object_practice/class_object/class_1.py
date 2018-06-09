#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 5/28/18

# class


# class Oldboystudent:
#     school = 'oldboy' #数据属性
#
#     def learn(self):#函数属性
#         print('is learning')
#
#     def eat(self):
#         print('is eating')
#
#     def play(self):
#         print('is learning')
#     # print('===run===')

#查看类的名称空间
# print(Oldboystudent.__dict__)
# print(Oldboystudent.__dict__['school'])
#查
# print(Oldboystudent.school)
# print(Oldboystudent.eat)
#
# #增
# Oldboystudent.country = 'China'
# print(Oldboystudent.__dict__)
#
# #删除
# del Oldboystudent.country
# print(Oldboystudent.__dict__)
#
# #改
# Oldboystudent.school = 'luffy'
# print(Oldboystudent.__dict__)


class Oldboystudent:
    school = 'oldboy' #数据属性

    def __init__(self,name,sex,age):  #__init__方法用来为对象定制对象自己独特的特征
        self.name = name
        self.age = age
        self.sex = sex

    def learn(self):#函数属性
        print('is learning')

    def eat(self):
        print('is eating')

    def play(self):
        print('is learning')


#产生对象
s1=Oldboystudent('李坦克','男',18) #先调用类产生空对象s1，然后调用OldboyStudent.__init__(s1,'李坦克','男',18)
s2=Oldboystudent('王大炮','女',38)
s3=Oldboystudent('牛榴弹','男',78)

#对象属性查看
# print(s3.name)

#改
s3.name = '里里'
print(s3.name)

#删除
del s3.name

print(s3.__dict__)

#增加

s3.class_name = 'python'

print(s3.__dict__)
