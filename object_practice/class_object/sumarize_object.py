#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 5/29/18


class Chinese:
    country = 'China'
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def eat(self):
        print('%s is eating' %self.name)

p1=Chinese('egon',18,'male')
p2=Chinese('alex',38,'female')
p3=Chinese('wpq',48,'female')

print(p3.country)

p3.eat()
