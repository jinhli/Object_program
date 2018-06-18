#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 6/14/18

from os import getcwd,path
from sys import path as sys_path
import sys
sys_path.insert(0,path.dirname(getcwd()))
from core.util import print_log
from core.Management import Management
from core.Student import Student
from core.Teacher import Teacher
from core.School import School
from core.Mypickle import Mypickle
from core.School import Course, Classes, School
from conf.setting import *
from core.util import print_log

def login():
    """
    登陆函数
    :return:
    """
    retry_count = 0
    while retry_count < 3:
        account = input('please input your account->').strip()
        password = input('please input your password->').strip()
        with open(user_account) as f:
            for line in f:
                user,pwd,role= line.split('|')
                if account == user and password ==pwd:
                    print_log('登陆成功', 'info')
                    return {"username":user,'role':role}
            retry_count += 1
    else:
        print_log("[%s]账户太多次尝试" %account)
        # log_obj.error("[%s]账户太多次尝试" % account)  # log type
        exit()


def main():
    """
    打印欢迎信息
    login: 得到的返回值，用户姓名和身份
    :return:
    """
    print_log('欢迎登陆选课系统','info')
    ret = login() #登陆 #ret = {'username':'eval','role':'Manager'}
    ret['role']=ret['role'].strip('\n')
    if ret:
        print(ret['username'],ret['role'])
        role_class = getattr(sys.modules[__name__],ret['role']) # 得到 类名
        obj = role_class(ret['username'])
        while True:
            for i,j in enumerate(role_class.menu,1):
                # print(i,j[0])
                print('\033[32;1m%s %s\033[0m' %(i,j[0]))
        # try:
            ret=int(input('请输入操作序号'))
            if role_class.menu[ret-1][1] == 'exit':
                exit('退出系统')
            else:
                getattr(obj,role_class.menu[ret-1][1])()
        # except:
        #     print_log('对不起，输入不正确','error')
main()

