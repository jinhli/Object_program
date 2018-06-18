#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 6/18/18


from os import getcwd,path
from sys import path as sys_path
sys_path.insert(0,path.dirname(getcwd()))


from core.School import Course, Classes, School
from core.Mypickle import Mypickle
from conf.setting import *
from core.util import print_log

class Role:
    def __init__(self,name):
        self.name = name
        self.school = None
        self.clas = None
        self.course = None


    def show(self):
        print(self.name)

    @staticmethod
    def boundClass(obj):
        school_obj = School.getObj(obj.school,schoolinfo)  #获得school实例 ，如北京校区

        school_obj.showSchoolClass
        class_name = input('请输入要绑定的班级>>:').strip()
        class_obj = School.getObj(class_name,classinfo)
        obj.clas = class_obj
        print(obj.clas)
        # Mypickle(self.clas.student_path).edit(self)
        print_log('绑定班级成功', 'info')


# class Teacher(Role):
#     menu = [('查看学生列表', 'show_student'), ('修改学生成绩', 'modify_core'),('选班级','teachClass'),('显示已选班级','showOweClass'),('退出','exit')]
#     def __init__(self,name):
#         super().__init__(name)
#
#     def teacherClass(self):
#         super().boundClass()
#
# class Student(Role):
#     menu = [('缴费', 'payment'),('选班级','studentClass'),('退出','exit')]
#     budget = 15000
#
#     def __init__(self,name):
#         super().__init__(name)
#         self.score = None
#
#     def studentClass(self):
#         super().boundClass()


# Tea = Teacher('alex')
# Tea.school = '北京校区'
# Tea.show()
#
# print(Tea.clas)
# Tea.boundClass()
# print(Tea.clas)

# Stu = Student('bonnie')
# Stu.school = '北京校区'
# print(Stu.clas,Stu.school,Stu.score)
# Stu.boundClass()
# print(Stu.clas,Stu.school,Stu.score)