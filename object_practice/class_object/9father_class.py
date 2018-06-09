#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 5/30/18

# class ParentClass1: #定义父类
#     pass
#
# class ParentClass2: #定义父类
#     pass
#
# class SubClass1(ParentClass1): #单继承，基类是ParentClass1，派生类是SubClass
#     pass
#
# class SubClass2(ParentClass1,ParentClass2): #python支持多继承，用逗号分隔开多个继承的类
#     pass
#
# print(SubClass1.__bases__)
# print(SubClass2.__bases__)

#派生
# class Hero:
#     def __init__(self,nickname,life_value,aggresivity):
#         self.nickname = nickname
#         self.life_value = life_value
#         self.aggresivity = aggresivity
#
#     def attack(self,enemy):
#         enemy.life_value -= self.aggresivity
#
# class Garen(Hero):
#     camp = 'Demacia'
#     pass
#
#
#
#
# class Riven(Hero):
#     camp = 'Noxus'  #派生出新的属性
#     pass
#
#
# g1 = Garen('草丛人',100,30)
# r1 = Riven('可爱的人',80,50)
#
# print(Riven.__dict__)
# print(r1.nickname, r1.camp)

#继承

# class Foo:
#     def f1(self):
#         print('Foo.f1')
#
#     def f2(self):
#         print('Foo.f2')
#         self.f1()
#
# class Bar(Foo):
#     def f1(self):
#         print('Bar.f1')
#
#
# b=Bar()
# b.f2()

# #继承实现原理
class G(object):
    def test(self):
        print('from G')

class I(G):
    def test(self):
        print('from I')

class F(I):
    def test(self):
        print('from F')

class H(G):
    def test(self):
        print('from H')

class E(H):
    def test(self):
        print('from E')

class D(G):
    def test(self):
        print('from D')

class C(F):
    def test(self):
        print('from C')

class B(E):
    def test(self):
        print('from B')

class A(B,C,D):
    # def test(self):
    #     print('from F')
    pass

# #A->B->E->H->C->F->I->D ->G #一条到走到倒数第二个副类，然后再找第二条道
# f1=F()
# f1.test()
# print(A.__mro__)