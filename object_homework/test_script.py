#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 6/16/18


#     # python = Course('python', '4月', 5400, '北京校区')
#     # linux = Course('linux', '8月', 8400,'北京校区')
#     shanghai = School('上海校区')
#     go = Course('go', '3月', 5400,'上海校区')
#     go.school.course.append(go.name)
#     # beijing = School('北京校区')
#     # beijing.course.append(python)
#
#     # shanghai.course.append(go)
# #
# #     school_list =[beijing,shanghai]
# #
# #     for i in school_list:
#     school_pickle.dump(shanghai)
# #
#     # course_list = [python, linux, go]
#     # for i in course_list:
#     course_pickle.dump(go)
#
#
#
# # beijing.course.append(python)  #组合的用法
# # shanghai.course.append(go)
#
# # Classes1 = Classes('上海','s109','python') #组合
# # print(Classes1.school.name)
# # print(Classes1.school.course)
# # print(shanghai.name)
#
# # print(beijing.course)
# # print(shanghai.course)
#
# # beijing = School('北京', [python,linux])
# # shanghai = School('上海' , [go])
# # python_class = Classes('北京', 's109', 'python', student_path)  #student_path =  path.join(studentinfo,class_name
# # class_pickle = Mypickle(classinfo)
# # class_pickle.dump(python_class)
#
# # if hasattr(python,'name'):  #反射
# #     res = getattr(python,'price')
# #     print(res)
#
#
#
# #
# class_info = school_pickle.loaditer() #生成器
# for class_obj in class_info: #一条记录就是一个对象， class_info 有很多对象
#     for i in class_obj.__dict__.keys():
#         print(i,class_obj.__dict__[i])  #打印一条对象
#
#
#
#
# shanghai = School('上海校区')
# beijing = School('北京校区')
# python = Course('python', '4月', 5400)
# go = Course('go', '3月', 5400)
# linux = Course('linux', '8月', 8400)
# python_class = Classes('s109','北京',  'python', 'student_path')
#
# #
# # print(shanghai.course,beijing.course)
#
# # shanghai.add_class(python_clas)
# beijing.add_class(python_class)
# beijing.add_course(python)
# # beijing.course.append(python)
#
# print(beijing.clas[0].student_path)
# print(beijing.course[0].period,beijing.name)

# class_name = input('请输入要绑定的班级>>:').strip()
# load_info = Mypickle(classinfo).loaditer()  # 加载课程对象
# for item_info in load_info:
#     if item_info.__dict__['name'] == class_name:  # 课程对象
#         self.classes = item_info  # 课程对象，而不是课程名字
#         Mypickle(teacher_obj).edit(self)
#         print_log('绑定班级成功', 'info')
