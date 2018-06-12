#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 6/10/18


import pickle
#




def file_oper(file, mode, *args):
    # 数据库写入、读取操作

    if mode == "ab":
        with open(file, mode) as f:
            # dict2 = args[0]
            dict2 = 'alex|123|0|role' + '\n'
            pickle.dump(dict2, f)


    if mode == "rb":  #pickle 数据需要用pickle 写入，再load
        with open(file, mode) as f:

            dict1 = pickle.load(f)
            # print(dict1)
            return dict1


file_oper('account_file.txt','ab')
dict_1 = file_oper('account_file.txt', 'rb')
dict_2 = file_oper('account_file.txt', 'rb')
print(dict_1,dict_2)


