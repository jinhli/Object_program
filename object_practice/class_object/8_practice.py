#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 5/29/18

#练习一
#
# class Student:
#     school = 'luffycity'
#     count = 0
#
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         Student.count +=1
#
#     def learn(self):
#         print("%s is learning" %self.name)
#
#
# stu1 = Student('alex',38,'male')
# stu2 = Student('egon',18,'male')
# stu3 = Student('bonnie',30,'female')
#
# print(Student.count)

#练习2
# 练习2：模仿王者荣耀定义两个英雄类， (10分钟)
#
# 要求：
#
# 英雄需要有昵称、攻击力、生命值等属性；
# 实例化出两个英雄对象；
# 英雄之间可以互殴，被殴打的一方掉血，血量小于0则判定为死亡。


class Garen:
    camp = 'Demacia'

    def __init__(self,nickname,life_value,aggresivity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggresivity = aggresivity

    def attack(self,enemy):
        enemy.life_value -= self.aggresivity


class Riven:
    camp = 'Noxus'

    def __init__(self, nickname, life_value, aggresivity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggresivity -= aggresivity

    def attack(self, enemy):
        enemy.life_value = self.aggresivity

g1 = Garen('草丛人',100,30)
r1 = Riven('可爱的人',80,50)