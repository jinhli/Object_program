#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Bonnie Li"
# Email: bonnie922713@126.com
# Date: 6/10/18

import pickle
import os


#写一个通用类，可以用来处理所有数据，保存，修改，读取

class Mypickle:
    def __init__(self,filename ):
        self.filename = filename

    def dump(self, obj):  #dump 文件
        with open(self.filename,'ab') as f:
            pickle.dump(obj,f, 1)

    def loaditer(self): # 取文件内容
        with open(self.filename, 'rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    yield obj
                except:
                    break

    def edit(self, obj): #修改
        f2 = Mypickle(self.filename+'.bak')
        for item in self.loaditer():
            if item.name == obj.name:
                f2.dump(obj)
            else:
                f2.dump(item)
        os.replace(self.filename+'.bak', self.filename)


    def delInfo(self,obj): # 删除在原来课程中的信息
        f2 = Mypickle(self.filename + '.bak')
        for item in self.loaditer():
            if item.name != obj.name:
                f2.dump(item)
            else:
                print('删除在原班级的信息')
        if not os.path.exists(self.filename + '.bak'):
            open(self.filename + '.bak', 'w').close()   #如果文件不存在， 就建一个空文件
        os.replace(self.filename + '.bak', self.filename)








