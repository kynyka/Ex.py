# -*- coding:utf-8 -*-
import sys
import math
import time
# newPath = "D:/Exercises/Ex.py/oldBoy/d03/files"
# if newPath not in sys.path:
#     sys.path.append(newPath)
# print 'index:', __name__
# print sys.path
# from files import demo

# demo.Foo()
# a = {'1' : 'a', '2' : 'b', '3' : 'c', '4' : 'd'}
# e = {v: k for k, v in a.iteritems()}
# print e
# def log(func):
#     def wrapper(*args, **kwargs):
#         print('call %s()' % func.__name__)
#         return func(*args, **kwargs)
#     return wrapper

# @log
# def func():
#     print 'do something'

# func()
from threading import Thread
import time

def Foo(arg,v):
    for i in range(10):
        print i
        time.sleep(1)

print 'before'
t1 = Thread(target=Foo, args=('kkjkjkj',1,))
t1.start()
print t1.getName()
t1.join(5)
print 'after'
