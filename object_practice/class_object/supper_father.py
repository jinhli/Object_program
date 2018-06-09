#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 5/31/18

#子类中重用父类属性
#
# class Hero:
#     def __init__(self,nickname,life_value,aggresivity):
#         self.nickname = nickname
#         self.life_value = life_value
#         self.aggresivity = aggresivity
#
#     def attack(self, enemy):
#         enemy.life_value -= self.aggresivity
#
# class Garen(Hero):
#     camp = 'Demacia'
#     def __init__(self,nickname,life_value,aggresivity,weapon):
#         super().__init__(nickname,life_value,aggresivity)
#         self.weapon = weapon
#
#     def attack(self, enemy):
#         super().attack(enemy)
#         print('%s attach %s  with %s' %(g1.nickname,r1.nickname,g1.weapon))
#
# g1 = Garen('草丛人',100,30,"金箍棒")
# r1 = Garen('可爱的人',80,50,'烽火轮')
#
# print(r1.life_value)
# g1.attack(r1)
# print(r1.life_value)


class A:
    def f1(self):
        print('from A')
        super().f1()


class B:
    def f1(self):
        print('from B')


class C(A,B):
    pass



print(C.mro())
#[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

c = C()
c.f1()
























