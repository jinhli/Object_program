#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 6/18/18
from core.School import *
from conf.setting import *
# from core.Mypickle import Mypickle

class Role:
    def __init__(self,name):
        self.name = name
        self.school = None
        self.clas = None
        self.course = None

    def show(self):
        print(self.name)

    @staticmethod
    def getObj(obj_name, obj_name_file):
        load_info = Mypickle(obj_name_file).loaditer()  # 加载课程对象
        for item_info in load_info:
            if item_info.__dict__['name'] == obj_name:  # 课程对象
                return item_info

    def boundClass(self):
        school_obj = Role.getObj(self.school, schoolinfo)  # 获得school实例 ，如北京校区
        school_obj.showSchoolClass
        class_name = input('请输入要绑定的班级>>:').strip()
        class_obj = Role.getObj(class_name, classinfo)
        self.clas = class_obj



