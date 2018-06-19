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
import os.path


class Student(Role):
    menu = [('缴费', 'payment'), ('更换班级', 'boundClass'), ('退出', 'exit')]
    budget = 15000

    def __init__(self, name):
        super().__init__(name)
        self.score = None

    def payment(self):  # 缴费
        # print(self.clas,self.score, self.budget)
        print('选定的课程>>:%s' % self.course)
        course_info = Mypickle(course_obj).loaditer()
        for course in course_info:
            if self.course == course.__dict__['name']:
                class_price = course.__dict__['price']
                print('课程价格>>:%s' % class_price)
                self.budget = self.budget - int(class_price)
                print(self.budget)
        stu_path = path.join(studentinfo, self.clas)
        Mypickle(stu_path).edit(self)
        print('缴费成功，剩余金额是>>:%s' % self.budget)

    def boundClass(self):  # 默认管理员会设置班级， 但是可以自己选 班级
        print('你目前所在的班级>>:%s' % self.clas)
        super().boundClass()
        stu_path = path.join(studentinfo, self.clas)
        Mypickle(stu_path).edit(self)
        print_log('绑定班级成功', 'info')



