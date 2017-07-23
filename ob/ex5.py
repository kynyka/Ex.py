# -*- coding:utf-8 -*-
from threading import Thread
import time

class MyThread(Thread):

    def run(self):
        time.sleep(5)
        print '我是线程'

def Bar():
    print 'bar'

t1 = MyThread(target=Bar)
t1.start()
print 'over'


# from threading import Thread
# import time

# def Foo(arg,v):
#     for i in range(10):
#         print i
#         time.sleep(1)

# print 'before'
# t1 = Thread(target=Foo, args=('kkjkjkj',1,))
# t1.start()
# print t1.getName()
# t1.join(5)
# print 'after'