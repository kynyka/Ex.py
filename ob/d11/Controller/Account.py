# -*- coding:utf-8 -*-

def Login():
    # open打开html文件
    # 从内存读取html文件
    # 数据库比较 用户名、密码 ==> 会用到Model
    # 返回给用户信息 ==> 会用到View
    f = open('D:/Exercises/Ex.py/ob/d11/View/login.html', 'r')
    data = f.read()

    return data

def Logout():
    return 'logout'