# -*- coding:utf-8 -*-
from threading import Thread
from Queue import Queue
import time

class Producer(Thread):

    def __init__(self, name, queue):
        '''
        @param name: 生产者的名称
        @param queue: 容器
        '''
        self.__Name = name
        self.__Queue = queue
        super(Producer, self).__init__()  # 执行父类的构造函数

    def run(self):
        while True:
            if self.__Queue.full():
                time.sleep(2)
            else:
                self.__Queue.put('baozi')
                time.sleep(1)
                print '%s 生产了一个包子' % (self.__Name,)
        Thread.run(self)


class Consumer(Thread):

    def __init__(self, name, queue):
        self.__Name = name
        self.__Queue = queue
        super(Consumer, self).__init__()

    def run(self):
        while True:
            if self.__Queue.empty():
                time.sleep(1)
            else:
                self.__Queue.get()
                print '%s 消费了一个包子' % (self.__Name,)
                time.sleep(1)
        self.__Queue.get()
        Thread.run(self)

que = Queue(maxsize=100)  # 空的大盘子 顶多放100个包子

alex1 = Producer('alex1', que)  # 相当于一个线程
alex1.start()
alex2 = Producer('alex2', que)  # 相当于一个线程
alex2.start()
alex3 = Producer('alex3', que)  # 相当于一个线程
alex3.start()

for i in range(20):
    name = 'eric%d' % (i,)
    temp = Consumer(name, que)
    temp.start()


'''
print que.qsize()
que.put('1')
que.put('2')
print 'empty:', que.empty()
print que.qsize()
print 'get:', que.get()  # 队列已是先进先出结构 故get不需要参数了
print 'get:', que.get()
print 'empty:', que.empty()
'''
