#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 6/11/18

from os import getcwd,path
from sys import path as sys_path
sys_path.insert(0,path.dirname(getcwd()))

BASE_DIR = path.dirname(path.dirname(path.abspath(__file__))) #整个程序的主目录

schoolinfo = '%s/db/schoolinfo'%BASE_DIR
classinfo = '%s/db/classinfo'%BASE_DIR
course_obj = '%s/db/course_obj'%BASE_DIR
studentinfo = '%s/db/studentinfo'%BASE_DIR  #这是一个目录， 其他的都是文件
teacher_obj = '%s/db/teacher_obj'%BASE_DIR
user_account = '%s/db/user_account'%BASE_DIR







