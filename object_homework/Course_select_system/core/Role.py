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

    def boundClass(self):
        school_obj = School.getObj(self.school, schoolinfo)  # 获得school实例 ，如北京校区
        school_obj.showSchoolClass
        class_name = input('请输入要绑定的班级>>:').strip()
        class_obj = School.getObj(class_name, classinfo)
        self.clas = class_obj



