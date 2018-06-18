#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 6/10/18




class Role:
    def __init__(self,name,school,course,class1):
        self.name = name
        # self.age = age
        # self.sex = sex
        self.school = school
        self.course = course
        self.class1 = class1


class Student(Role):
    def __init__(self, name, school,course,class1,score):
        super().__init__(name,school,course,class1)
        self.score = score


    def register(self):
        pass


    def payment(self):
        pass

    def choose_class(self):
        pass




class Teacher(Role):
    def __init__(self,name,course,school, class1):
        super().__init__(name,school,course,class1 )


    def manage_class(self): #查看学生列表，
        pass


    def modify_score(self): #修改学生成绩
        pass

    def choose_class(self): #选班级
        pass


class Account: #账号类
    def __init__(self,account_name,password,status,role):
        self.account_name = account_name
        self.password = password
        self.status = status
        self.role  = role



