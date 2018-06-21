#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 6/12/18

from core.Role import Role
from core.util import print_log
from core.Mypickle import Mypickle
from conf.setting import *


class Teacher(Role):
    menu = [('查看学生列表', 'show_student'), ('修改学生成绩', 'modify_score'), ('选班级', 'boundClass'), ('退出', 'exit')]

    def __init__(self, name):
        super().__init__(name)

    def boundClass(self):
        print('当前绑定的班级>>:%s' % self.clas)
        super().boundClass()
        Mypickle(teacher_obj).edit(self)
        print_log('绑定班级成功', 'info')

    def show_student(self):  # 查看学生列表
        if self.clas:
            path = self.clas.student_path
            load_info = Mypickle(path).loaditer()
            for item_info in load_info:
                for i in item_info.__dict__.keys():
                    if i != 'clas' and i != 'budget':
                        print(i, item_info.__dict__[i])
                print('-' * 50)
        else:
            print_log('你没有绑定任何班级')

    def modify_score(self):  # 修改学生成绩
        student_name = input('输入要修改成绩的学生姓名>>:').strip()
        student_score = input('输入成绩>>:').strip()
        if self.clas:
            stu_path = self.clas.student_path
            load_info = Mypickle(stu_path).loaditer()  # 加载的是学生对象
            for item_info in load_info:
                if item_info.__dict__['name'] == student_name:
                    item_info.__dict__['score'] = student_score
                    Mypickle(stu_path).edit(item_info)  # 保存的是学生对象
                else:
                    print_log('你输入的学生不在该班级','error')
        else:
            print_log('你还没有绑定班级', 'error')










