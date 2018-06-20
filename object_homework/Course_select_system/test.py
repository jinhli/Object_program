#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 6/14/18

# class People:
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#
# class Course:
#     def __init__(self,name,period,price):
#         self.name=name
#         self.period=period
#         self.price=price
#     def tell_info(self):
#         print('<%s %s %s>' %(self.name,self.period,self.price))
#
# class Teacher(People):
#     def __init__(self,name,age,sex,job_title):
#         People.__init__(self,name,age,sex)
#         self.job_title=job_title
#         self.course=[]
#         self.students=[]
#
#
# class Student(People):
#     def __init__(self,name,age,sex):
#         People.__init__(self,name,age,sex)
#         self.course=[]
#
#
# egon=Teacher('egon',18,'male','沙河霸道金牌讲师')
# s1=Student('牛榴弹',18,'female')
#
# python=Course('python','3mons',3000.0)
# linux=Course('python','3mons',3000.0)
#
# #为老师egon和学生s1添加课程
# egon.course.append(python)
# egon.course.append(linux)
# s1.course.append(python)
#
# #为老师egon添加学生s1
# egon.students.append(s1)
#
#
# #使用
# for obj in egon.course:
#     obj.tell_info()

# from os import getcwd,path
# from sys import path as sys_path
# sys_path.insert(0,path.dirname(getcwd()))
#
# from conf.setting import *
# from core.Management import Management
#
#
# class Student(Management):
#     course = 'python'
#     def __init__(self,name,clas):
#         super().__init__(name)
#         self.clas = clas
#
#
# stu1= Student('bonnie','s91')
# print(stu1.__dict__)
# stu1.school_pickle_obj.loaditer()

# from os import getcwd,path
# from sys import path as sys_path
# sys_path.insert(0,path.dirname(getcwd()))
#
#
# from core.School import Course, Classes, School
# from core.Mypickle import Mypickle
# from conf.setting import *
# from core.Management import Management
#
# stu_path=r'/home/bonnie/python_learning/pycharm_project/5_object/object_homework/Course_select_system/db/studentinfo/s91'
# #
# clas1= Clas('s91','python',stu_path)
# student1= Student('huahua','shanghai')
# student1.classes = clas1
# student1.show_student()

# load_info = Mypickle(stu_path).loaditer()
# for item_info in load_info:
#     for i in item_info.__dict__.keys():
#         print(i, item_info.__dict__[i])
#     print('-' * 50)

# pickle_obj = getattr(self, pickle_obj)

# class Management:
#     menu = [('创建学校','create_school'),('创建老师账号','create_teacher'), ('创建学生账号','create_student'), ('创建课程','create_course'),('创建班级','create_classes'),
#             ('显示老师信息','show_teacher'), ('显示学校','show_school'), ('显示课程','show_course'),('显示班级','show_classes'),
#             ('绑定班级', 'bound_class'),('退出','exit')]
#     def __init__(self,name):
#         self.name = name
#         self.teacher_pickle_obj = Mypickle(teacher_obj)
#         self.course_pickle_obj = Mypickle(course_obj)
#         self.school_pickle_obj = Mypickle(schoolinfo)
#         self.class_pickle_obj = Mypickle(classinfo)
#
#
#     def show(self, pickle_obj):
#         pickle_obj = getattr(self, pickle_obj)
#
#         load_info = pickle_obj.loaditer()
#         for item_info in load_info:
#             print('我找到了')
#             for i in item_info.__dict__.keys():
#                 print(i, item_info.__dict__[i])
#             print('-' * 50)
#
#     def show_school(self):
#         print('please list all the school')
#
#         self.show('school_pickle_obj')
#
#
# m1= Management('mm')
# m1.show_school()


# def transfer(**kwargs):
#     print(kwargs.keys())
#     list1 = list(kwargs.keys())
#     print(list1[0])
#
#
# transfer(course='python')class A:
# #     def __init__(self,name):
# #         self.name = name
# #
# #
# #     # def exit(self):
# #     #     exit('leave the system')
# # a = A('mim')
# # # a.exit()
# #
# # print(A.__dict__)


#

# from core.School import Course, Classes, School
# from core.Teacher import Teacher
# from core.Student import Student
# from core.Mypickle import Mypickle
# from conf.setting import *
# from core.util import print_log
#
# # @staticmethod
# def getObj(obj_name,obj_name_file):
#     load_info = Mypickle(obj_name_file).loaditer()  # 加载课程对象
#     for item_info in load_info:
#         if item_info.__dict__['name'] == obj_name:  # 课程对象
#             return item_info
#
# #
# # obj = getObj('北京校区',schoolinfo)
# obj=getObj('nini',teacher_obj)
# # print(obj.name,obj.cl)
#
# class Vehicle:  # 定义交通工具类
#     Country = 'China'
#
#     def __init__(self, name, speed, load, power):
#         self.name = name
#         self.speed = speed
#         self.load = load
#         self.power = power
#
#     def run(self):
#         print('开动啦...')
#
#
# class Subway(Vehicle):  # 地铁
#     def __init__(self, name, speed, load, power, line):
#         # super(Subway,self) 就相当于实例本身 在python3中super()等同于super(Subway,self)
#         super().__init__(name, speed, load, power)
#         self.line = line
#
#     def run(self):
#         print('地铁%s号线欢迎您' % self.line)
#         super(Subway, self).run()
#
#
# class Mobike(Vehicle):  # 摩拜单车
#     pass
#
#
# line13 = Subway('中国地铁', '180m/s', '1000人/箱', '电', 13)
# line13.run()
# print(line13.Country)