#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 6/12/18

from os import getcwd,path
from sys import path as sys_path
sys_path.insert(0,path.dirname(getcwd()))

from core.School import Course, Classes, School
from core.Student import Student
from core.Mypickle import Mypickle
from conf.setting import *
from core.util import print_log
from core.Role import Role





class Teacher(Role):
    menu = [('查看学生列表', 'show_student'), ('修改学生成绩', 'modify_score'),('选班级','teacherClass'),('显示已选班级','showOweClass'),('退出','exit')]
    def __init__(self,name):
        super().__init__(name)

    def teacherClass(self):
        teacher_obj = School.getObj(self.name, teacher_obj)
        Role.boundClass(teacher_obj)

    def show_student(self): #查看学生列表
        if self.clas:
            path = self.clas.student_path
            load_info = Mypickle(path).loaditer()
            for item_info in load_info:
                for i in item_info.__dict__.keys():
                    if i != 'clas':
                        print(i, item_info.__dict__[i])
                print('-' * 50)
                print('show student')
        else:
            print_log('你没有绑定任何班级')




    def modify_score(self): #修改学生成绩
        student_name = input('输入要修改成绩的学生姓名>>:').strip()
        student_score = input('输入成绩>>:').strip()
        if self.clas:
            path = self.clas.student_path
            load_info = Mypickle(path).loaditer() #加载的是学生对象
            for item_info in load_info:
                if item_info.__dict__['name'] == student_name:
                    item_info.__dict__['score'] = student_score
                    Mypickle(path).edit(item_info) #保存的是学生对象
                else:
                    print_log('你输入的学生不在该班级')

    # def bound_class(self):
    #     school_obj = School.getObj(self.school,schoolinfo)  #获得school实例 ，如北京校区
    #     print(type(school_obj))
    #     school_obj.showSchoolClass()
    #     class_name = input('请输入要绑定的班级>>:').strip()
    #     print('before>>%s' %self.clas)
    #     self.clas = class_name  # 课程对象，而不是课程名字
    #     print('after>>%s' %self.clas)
    #     print(self.name)
    #     Mypickle(teacher_obj).edit(self)
    #     print_log('绑定班级%s成功' %self.clas, 'info')

    def showOweClass(self): #显示我选的班级

        teacher_obj = School.getObj(self.name, teacher_obj)
        print_log('关联的班级>>:%s' %teacher_obj.clas)

        # class_name = input('请输入要绑定的班级>>:').strip()
        # load_info = Mypickle(classinfo).loaditer() #加载课程对象
        # for item_info in load_info:
        #     if item_info.__dict__['name']== class_name: #课程对象





#
#
# stu_path=r'/home/bonnie/python_learning/pycharm_project/5_object/object_homework/Course_select_system/db/studentinfo/M91'
# clas2= Clas('M91','python',stu_path)
# Mypickle(classinfo).dump(clas2)
# teache1 = Teacher('alex')
# teache1.bound_class()

# load_info = Mypickle(teacher_obj).loaditer()
# for item_info in load_info:
#     for i in item_info.__dict__.keys():
#         print('------')
#         print(i, item_info.__dict__[i])
#     print('-' * 50)
# teache = []
# for item_info in load_info:
#     teache.append(item_info)

# teache1.show_student()
# teache1.modify_score()
# teache1.show_student()



