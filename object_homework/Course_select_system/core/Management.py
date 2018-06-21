#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 6/13/18
from os import path
from core.Mypickle import Mypickle
from conf.setting import *
from core.Student import Student
from core.Teacher import Teacher
from core.util import print_log
from core.Role import Role
from core.School import *

class Management:
    menu = [('创建学校','create_school'),('创建老师账号','create_teacher'), ('创建学生账号','create_student'), ('创建课程','create_course'),('创建班级','create_classes'),
            ('显示老师信息','show_teacher'), ('显示学校','show_school'), ('显示课程','show_course'),('显示班级','show_classes'),('退出','exit')]

    def __init__(self, name):
        self.name = name
        self.teacher_pickle_obj = Mypickle(teacher_obj)
        self.course_pickle_obj = Mypickle(course_obj)
        self.school_pickle_obj = Mypickle(schoolinfo)
        self.class_pickle_obj = Mypickle(classinfo)

    @staticmethod
    def userinfo_handle(content):  # 存储user_account 数据
        with open(user_account,'a')as f:
            f.write('\n%s' %content)

    def create_method(self):  # create 方法，创建学生和老师，并保存
        name = input('请输入姓名>>:').strip()
        password = input('请输入密码>>:').strip()
        role = input('please input the role>>:').strip()
        self.show_school()
        school = input('请输入学校>>:').strip()
        content = '%s|%s|%s' %(name,password,role)
        Management.userinfo_handle(content)
        return name,school

    def bound_school(self,school,**kwargs):
        key = list(kwargs.keys())[0]
        value= kwargs[key]
        school_info = self.school_pickle_obj.loaditer()  # 生成器
        for school_obj in school_info:  # 一条记录就是一个对象， class_info 有很多对象
            if school_obj.__dict__['name'] == school:
                school_obj.__dict__[key].append(value)
                school_obj1 = school_obj
                print(school_obj1.name,school_obj1.course)
        self.school_pickle_obj.edit(school_obj1)
        print_log('绑定学校成功','info')

    def create_teacher(self):
        name, school =self.create_method()        # 输入讲师的姓名， 输入讲师的密码， 将老师的信息写入user_account
        teacher_obj = Teacher(name)
        teacher_obj.school = school
        self.teacher_pickle_obj.dump(teacher_obj)
        print_log('创建成功', 'info')
        return

    def create_student(self):
        name, school =self.create_method()        # 输入的学生姓名，密码， 将信息写入user_account
        choose_course = input('请输入要学习的课程>>:').strip()
        choose_class = input('请输入所在的班级>>:').strip() #
        class_objs = self.class_pickle_obj.loaditer()
        for clas in class_objs:            #这里可以优化
            if clas.name == choose_class:
                stu_obj = Student(name)
                stu_obj.school = school
                stu_obj.clas = clas
                stu_obj.course = choose_course
                Mypickle(clas.student_path).dump(stu_obj)
                print_log('创建成功', 'info')
        # else:
        #     print_log('你输入的内容有错误，创建学生对象失败')

    def create_school(self):
        school = input('请输入学校>>:').strip()
        school_obj= School(school)
        self.school_pickle_obj.dump(school_obj)

    def create_classes(self):
        self.show_school()
        school = input('请输入学校>>:').strip()
        school_obj = Role.getObj(school, schoolinfo) #学校对象
        print('你所在学校的可选课程>>:%s ' % school_obj.course)
        course_name = input('请输入课程名称>>:').strip()
        class_name = input('请输入班级名称:').strip()
        student_path = path.join(studentinfo, class_name)
        open(student_path, 'w').close()
        class_obj = Classes(class_name, course_name, student_path)
        self.class_pickle_obj.dump(class_obj)
        school_obj.clas.append(class_obj.name)
        self.school_pickle_obj.edit(school_obj)
        print_log('创建成功', 'info')

    def create_course(self):
        self.show_school()
        school = input('请输入学校>>:').strip() # 学校不写入课程信息，用来判断课程应该写入到哪个学校
        name = input('请输入课程名称>>:').strip()
        period = input('请输入课程周期>>:').strip()
        price = input('请输入课程价格>>:').strip()
        course_obj = Course(name, period, price, school) # 生成一个课程对象
        self.course_pickle_obj.dump(course_obj) # 把课程对象写入到文件
        self.bound_school(school, course=course_obj)

    def show(self, pickle_obj):
        pickle_obj = getattr(self, pickle_obj)
        load_info = pickle_obj.loaditer()
        for item_info in load_info:
            for i in item_info.__dict__.keys():
                print(i,item_info.__dict__[i])
            print('-' * 50)

    def show_school(self):
        self.show('school_pickle_obj')  # 把字符串'school_pickle_obj'传到show, 然后show 通过反射，找到属性 Mypickle(schoolinfo)

    def show_teacher(self):
        self.show('teacher_pickle_obj')

    def show_classes(self):
        self.show('class_pickle_obj')

    def show_course(self):
        self.show('course_pickle_obj')


