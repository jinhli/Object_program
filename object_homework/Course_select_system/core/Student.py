#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 6/12/18

from os import getcwd,path
from sys import path as sys_path
sys_path.insert(0,path.dirname(getcwd()))


from core.School import Course, Classes, School
from core.Mypickle import Mypickle
from conf.setting import *
from core.util import print_log
from core.Role import Role




class Student(Role):
    menu = [('缴费', 'payment'),('退出','exit')]
    budget = 15000

    def __init__(self,name):
        super().__init__(name)
        self.score = None

    def payment(self): # 缴费

        print('选定的课程>>:%s' %self.course)  ##--> ?需要优化
        course_info = Mypickle(course_obj).loaditer()
        for course in course_info:
            if self.course == course.__dict__['name']:
                class_price = course.__dict__['price']
                self.budget =self.budget - int(class_price)
        print('缴费成功，剩余金额是>>:%s' %self.budget)


    # def select_class(self):  # 默认管理员会设置班级， 但是可以自己选 班级
    #     school_obj = School.getObj(self.school,schoolinfo)  #获得school实例 ，如北京校区
    #     school_obj.showSchoolClass
    #     class_name = input('请输入要绑定的班级>>:').strip()
    #     class_obj = School.geobj(class_name,classinfo)
    #     self.clas = class_obj
    #     Mypickle(self.clas.student_path).edit(self)
    #     print_log('绑定班级成功', 'info')



# stu_path=r'/home/bonnie/python_learning/pycharm_project/5_object/object_homework/Course_select_system/db/studentinfo/s91'
#
# clas1= Clas('s91','python',stu_path)
# student1= Student('huahua','shanghai')
# student1.classes = clas1
# student1.score = 90
# Mypickle(clas1.student_path).dump(student1)
# student1.show_student()

