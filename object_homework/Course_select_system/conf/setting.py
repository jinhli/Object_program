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
couse_obj = '%s/db/couse_obj'%BASE_DIR
student_obj = '%s/db/student_obj'%BASE_DIR
teacher_obj = '%s/db/teacher_obj'%BASE_DIR
user_account = '%s/db/user_account'%BASE_DIR







