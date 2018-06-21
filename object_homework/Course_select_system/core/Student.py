#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 6/12/18


from os import getcwd, path

from core.Role import Role
from core.util import print_log
from core.Mypickle import Mypickle
from conf.setting import *


class Student(Role):
    menu = [('缴费', 'payment'), ('更换班级', 'boundClass'), ('退出', 'exit')]


    def __init__(self, name):
        super().__init__(name)
        self.score = None
        self.budget = 15000

    def payment(self):  # 缴费
        # print(self.clas,self.score, self.budget)
        print('当前的余额>>:%s' % self.budget)
        print('选定的课程>>:%s' % self.course)
        course_info = Mypickle(course_obj).loaditer()
        for course in course_info:
            if self.course == course.__dict__['name']:
                course_price = course.__dict__['price']
                print('课程价格>>:%s' % course_price)
                budget = self.budget - int(course_price)
                if budget >= 0:
                    self.budget = budget
                    stu_path = path.join(studentinfo, self.clas.name)
                    Mypickle(stu_path).edit(self)
                    print('缴费成功，剩余金额是>>:%s' % self.budget)
                else:
                    print('缴费失败，余额不足 %s' %self.budget)



    def boundClass(self):  # 默认管理员会设置班级， 但是可以自己选 班级
        print('你目前所在的班级>>:%s' % self.clas.name)
        previous_clas = self.clas
        super().boundClass()
        stu_path = path.join(studentinfo, self.clas.name)
        stu_path1 = path.join(studentinfo,previous_clas.name)
        Mypickle(stu_path).dump(self)  # 把一个新对象加入到文件
        Mypickle(stu_path1).delInfo(self) #在原来班级信息中删除学生信息
        print_log('绑定班级成功', 'info')



# load_info = Mypickle(course_obj).loaditer()
# for item_info in load_info:
#     for i in item_info.__dict__.keys():
#         print(i, item_info.__dict__[i])
#     print('-' * 50)