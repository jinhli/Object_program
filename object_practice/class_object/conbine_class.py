#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 5/31/18

class People:
    school = 'luffycity'
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

class Course:
    def __init__(self,name,period,price):
        self.name=name
        self.period=period
        self.price=price
    def tell_info(self):
        print('<%s %s %s>' %(self.name,self.period,self.price))

class Teacher(People):
    def __init__(self,name,age,sex,job_title):
        super().__init__(name,age,sex)
        self.job_title=job_title
        self.course=[]
        self.students=[]


class Student(People):
    def __init__(self,name,age,sex):
        super().__init__(name,age,sex)
        self.course=[]

class Birth_date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    def tell_info(self):
        print("%s-%s-%s" %(self.year,self.month,self.day))


egon=Teacher('egon',18,'male','沙河霸道金牌讲师')
s1=Student('牛榴弹',18,'female')
d1 = Birth_date('1990','4','5')

s1.birt = d1
s1.birt.tell_info()

python=Course('python','3mons',3000.0)
linux=Course('linux','3mons',3000.0)


#
#为老师egon和学生s1添加课程
egon.course.append(python)
egon.course.append(linux)
s1.course.append(python)
s1.course.append(linux)
#
# #为老师egon添加学生s1
# egon.students.append(s1)
#
#
# #使用
for obj in s1.course:
    obj.tell_info()

