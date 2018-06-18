#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 6/12/18
from os import getcwd,path
from sys import path as sys_path
sys_path.insert(0,path.dirname(getcwd()))
from conf.setting import schoolinfo,classinfo,course_obj
from core.Mypickle import Mypickle
from conf.setting import *
#


class School:  # 创建学校
    def __init__(self,name):
        self.name = name
        self.course = []
        self.clas = []

    def showSchoolClass(self):  # 显示该实例下的班级
        class_obj_list = self.clas
        for class_obj in class_obj_list:
            print(class_obj.name)
        print('-' * 50)

    def showSchoolCourse(self):  # 显示实例下的课程信息
        course_obj_list = self.course
        for course_obj in course_obj_list:
            print(course_obj.name)
        print('-' * 50)

    @staticmethod
    def getObj(obj_name, obj_name_file):
        load_info = Mypickle(obj_name_file).loaditer()  # 加载课程对象
        for item_info in load_info:
            if item_info.__dict__['name'] == obj_name:  # 课程对象
                return item_info


class Course:  # create course
    def __init__(self,name,period,price,school):
        self.name = name
        self.period = period
        self.price = price
        self.school = school


    def __repr__(self):
        return self.name


class Classes:
    def __init__(self,name,course,student_path):
        self.name = name
        self.course = course
        self.student_path = student_path


    def __repr__(self):
        return self.name
#
# # # #
# if __name__=='__main__':
#     school_pickel=Mypickle(schoolinfo)
#     course_pickel = Mypickle(course_obj)
#     # 初始课程
#     python = Course('python', '4 months', 5400,'北京校区')
#     go = Course('go', '3 months', 5400,'上海校区')
#     linux = Course('linux', '3 months', 8400, '北京校区')
#     course_list = [python,linux, go]
#     for i in course_list:
#         course_pickel.dump(i)
#
#     #初始化校区
#     beijing = School('北京校区')
#     beijing.course.append(python)
#     beijing.course.append(linux)
#     shanghai = School('上海校区')
#     shanghai.course.append(go)
#
#     school_list=[beijing,shanghai]
#     for i in school_list:
#        school_pickel.dump(i)

# #


