#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 5/28/18

class Oldboystudent:
    school = 'oldboy' #数据属性

    def __init__(self,name,sex,age):  #__init__方法用来为对象定制对象自己独特的特征
        self.name = name
        self.age = age
        self.sex = sex

    def learn(self):#函数属性
        print('%s is learning' %self.name)

    def eat(self):
        print('%s is eating' %self.name)

    def play(self):
        print('%s is learning' %self.name)


#产生对象,私有特征
s1=Oldboystudent('李坦克','男',18) #先调用类产生空对象s1，然后调用OldboyStudent.__init__(s1,'李坦克','男',18)
s2=Oldboystudent('王大炮','女',38)
s3=Oldboystudent('牛榴弹','男',78)

# 对象：特征and 技能的结合点
# 类：一系列对象相似的特征和技能的结合体
# print(Oldboystudent.__dict__)

#类的数据属性：所有对象共有的


#类的函数属性：是绑定给对象，绑定到不同的对象是不同的绑定方法,对象调用绑定方式时，会把对象本省当作第一个传入，传给self
# Oldboystudent.learn(s1)
# Oldboystudent.learn(s2)
s1.learn()

