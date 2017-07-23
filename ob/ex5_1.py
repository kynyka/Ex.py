# -*- coding:utf-8 -*-
# 生产者消费者
import threading
import Queue
import time
import random


def Producer(name, que):
    while True:
    	if que.qsize() < 3:
        	que.put('baozi')
        	print '%s:Made a baozi...------------' % name
        else:
        	print u'还有3个包子'
        time.sleep(random.randrange(2))


def Consumer(name, que):
    while True:
    	try:
        	que.get_nowait()  # get是有阻塞的 这个就没阻塞了
        	print '%s: Got a baozi...' % name
        except Exception:
        	print u'没有包子了'
        time.sleep(random.randrange(3))

q = Queue.Queue()
p1 = threading.Thread(target=Producer, args=['chef1', q])
p2 = threading.Thread(target=Producer, args=['chef2', q])
p1.start()
p2.start()

c1 = threading.Thread(target=Consumer, args=['Alex', q])
c2 = threading.Thread(target=Consumer, args=['Eric', q])
c1.start()
c2.start()
