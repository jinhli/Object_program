作者:Bonnie Li
版本:示例版本 v0.1
程序介绍: 选课系统,可以参考流程图，和关系图
用到的知识点：类，实例化，继承，组合，绑定方法，非绑定方法，反射
├── bin
│   ├── __init__.py
│   └── start.py
├── conf
│   ├── __init__.py
│   └── setting.py
├── core
│   ├── __init__.py
│   ├── main.py
│   ├── Management.py
│   ├── Mypickle.py
│   ├── Role.py
│   ├── School.py
│   ├── Student.py
│   ├── Teacher.py
│   └── util.py
├── db
│   ├── classinfo
│   ├── course_obj
│   ├── __init__.py
│   ├── schoolinfo
│   ├── studentinfo
│   │   ├── __init__.py
│   │   ├── linux_s10
│   │   ├── python_s10
│   │   └── python_s11
│   ├── teacher_obj
│   └── user_account
└── README.md

使用：
运行bin文件夹的start.py
管理员用户：
alex|12345
老师用户：
nini|7890
egon|7890
shanshan|7890|Teacher
学生用户： 学生用户需要知道绑定的班级
bonnie|123456 ->python_s11
laowang|123456 ->linux_s10

