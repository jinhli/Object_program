#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 6/6/18

import setting
import hashlib
import time

#绑定方法和非绑定方法
# class Mysql:
#     def __init__(self,host,port):
#         self.host = host
#         self.port = port
#
#     @classmethod
#     def from_conf(cls):
#         # print(cls)
#         return cls(setting.HOST,setting.PORT)
#
#     @staticmethod
#     def create_id():
#         m = hashlib.md5(str(time.time()).encode('utf-8'))
#         return m.hexdigest()
#
# # print(Mysql.from_conf)
#
# conn = Mysql.from_conf()
# conn1 = Mysql('192.168.0.1',22 )
#
# print(conn.from_conf)
#
#
# print(conn1.host, conn1.port)
# print(conn1.create_id, Mysql.create_id)


#使用实例进行 获取、设置、删除 数据, 分别会触发类的什么私有方法

# class A:
#
#     def __init__(self,name):
#         self.name = name
#
#     def __setitem__(self, key, value):
#         self.__dict__[key] = value
#
#     def __getitem__(self, item):
#         print(self.__dict__[item])
#
#     def __delitem__(self, key):
#         print('del obj[key]')
#         self.__dict__.pop(key)
#
#     def __delattr__(self, item):
#         print('del obj.key')
#         self.__dict__.pop(item)
#
# f1 = A('sb')
# f1['age'] = 18
# f1['age1'] =28
# f1['name'] = 'bonnie'
# del f1.age1
# del f1['age']
# print(f1.__dict__)


# class P1():
#     def foo(self):
#         print('p1-foo')
#
#     def bar(self):
#         print('P1-bar')
#
#
# class P2():
#     def foo(self):
#         print('p2-foo')
#
#     def bar(self):
#         print('p2-bar')
#
# class P3():
#     pass
#
# class C1(P3,P1):
#     pass
#
#
# class C2(P2):
#     def bar(self):
#         print('C2-bar')
#     #pass
#
# class D(C1, C2):
#     pass
#
#
#
# d = D()
#
# print(D.mro())
# print(C1.mro())
# print(C2.mro())
#
# d.foo()
# d.bar()

#
# class Sql:
#     host= '127.0.0.1'
#     port=3306
#     db='db1'
#     charset='utf8'
#     sql='select * from tb1;'
#     proc_name='存储过程的名字'
#     def __init__(self,*args):
#         self.args=args
#     def connect(self):
#         pass
#
#     def exc(self):
#         if self.args == self.sql:
#             conn = self.connect(self.host,self.port,self.db,self.charset)
#             res=conn.execute(self.sql)
#             print('excute')
#             return res
#         elif self.args == self.proc_name:
#
#             conn = self.connect(self.host, self.port, self.db, self.charset, self.proc_name)
#             res = conn.call_proc(self.sql)
#             return res
# ex=Sql('select * from tb1;')
#
# ex.exc()

#
# class People(object):
#     __name = "luffy"
#     __age = 18
#
#
# p1 = People()
# print(p1._People__name, p1._People__age) #


# class People(object):
#
#    def __init__(self):
#        print("__init__")
#
#    def __new__(cls, *args, **kwargs):
#        print("__new__")
#        return object.__new__(cls, *args, **kwargs)
#
# People()




# class A(object):
#     def __init__(self,name):
#         self.name = name
#     def foo(self, x):
#        print("executing foo(%s, %s)" % (self,x))
#
#     @classmethod
#     def class_foo(cls, x):
#         print("executing class_foo(%s, %s)" % (cls,x))
#
#     @staticmethod
#     def static_foo(x):
#         print("executing static_foo(%s)" % (x))
#
#     @property
#     def proper_1(self):
#         print('hello, property')
#
# a = A('bonnie')
# print(a.name)
# a.foo('hello')
# A.class_foo('nihao')
# a.static_foo('nihao')
# a.proper_1



# class Dog(object):
#
#    def __init__(self,name):
#        self.name = name
#
#    @property
#    def eat(self):
#        print(" %s is eating" %self.name)
#
# d = Dog("ChenRonghua")
# d.eat

# import abc
#
# class Animal(metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def talk(self):
#         pass
#
# def func(obj):
#     obj.talk()
#
# class Dog(Animal):
#
#     def talk(self):
#         print('wangwang')
#
#
# class Cat(Animal):
#     def talk(self):
#         print('miaomiao')
#
#
# class People(Animal):
#     def talk(self):
#         print('Hello')
#
# cat1 = Cat()
# dog1 = Dog()
# People1 = People()
#
# print(isinstance(cat1,Cat))
#

#17
#
# class Role:
#     def __init__(self,name,life_value,attack_value):
#         self.name = name
#         self.life_value = life_value
#         self.attack_value = attack_value
#     def attack(self,enemy):
#         enemy.life_value -= self.attack_value
#
# class People(Role):
#
#     def attack(self,enemy):
#         super().attack(enemy)
#         print('%s attack %s' %(self.name, enemy.name))
#
#
# class Dog(Role):
#     def bite(self, enemy):
#         super().attack(enemy)
#         print('%s bite %s' %(self.name, enemy.name))
#
# dog1 = Dog('jiwawa',100,30)
# people1 = People('xiaoming',300,50)
#
# print(dog1.life_value)
# people1.attack(dog1)
# print(dog1.life_value)
# print(people1.life_value)
# dog1.bite(people1)
# print(people1.life_value)

# class Mymetaclass(type):
#     def __new__(cls,name,bases,attrs):
#         update_attrs={}
#         for k,v in attrs.items():
#             if not callable(v) and not k.startswith('__'):
#                 update_attrs[k.upper()]=v
#             else:
#                 update_attrs[k]=v
#         return type.__new__(cls,name,bases,update_attrs)
# class Chinese(metaclass=Mymetaclass):
#     country='China'
#     tag='Legend of the Dragon' #龙的传人
#     def __init__(self,name):
#         self.name = name
#     def walk(self):
#         print('%s is walking' %self.name)
# # print(Chinese.__dict__)
#
#
# c1 = Chinese('bonnie')
# c1.walk()
# print(c1.COUNTRY)


class Mymeta(type): #继承默认元类的一堆属性
    def __init__(self,class_name,class_bases,class_dic):
        if not class_name.istitle():
            raise TypeError('类名首字母必须大写')

        super(Mymeta,self).__init__(class_name,class_bases,class_dic)

    def __call__(self, *args, **kwargs):
        #self=People
        print(self,args,kwargs) #<class '__main__.People'> ('egon', 18) {}

        obj = self.__new__(self, *args, **kwargs)
        # self.__init__(obj,*args,**kwargs)
        return obj


class People(object,metaclass=Mymeta):
    country='China'

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def talk(self):
        print('%s is talking' %self.name)

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        cls.__init__(obj,*args, **kwargs)
        return obj

obj = People('bonnie',18)

print(obj.__dict__)