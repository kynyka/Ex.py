# -*- coding:utf-8 -*-
# thread_event 事件触发 类似JS的addListenerEvent
# import threading
# import time


# def producer():
#     print u'chef: 等人来买包子...'
#     event.wait()  # 这是个阻塞,等到ln19,OK,阻塞消失
#     event.clear()  # 将set()为True改回False状态
#     print u'chef: sb is coming for baozi...'

#     print 'chef: making a baozi for sb...'
#     time.sleep(3)


#     print u'chef: 你的包子好了'
#     event.set()  # 做好了告诉人家


# def consumer():
#     print u'alex: 去买包子...'
#     event.set()

#     time.sleep(2)
#     print 'alex: waiting for baozi to be ready'
#     print event.wait()

#     print u'alex: 哎呀真好吃'

# event = threading.Event()

# p = threading.Thread(target=producer)
# c = threading.Thread(target=consumer)

# p.start()
# c.start()

import threading
import time


def producer():
    print u'chef: 等人来买包子...'
    event.wait()  # 这是个阻塞,等到ln19,OK,阻塞消失
    event.clear()  # 将set()为True改回False状态
    print u'chef: sb is coming for baozi...'

    print 'chef: making a baozi for sb...'
    time.sleep(3)


    print u'chef: 你的包子好了'
    event.set()  # 做好了告诉人家


def consumer():
    print u'alex: 去买包子...'
    event.set()

    time.sleep(2)
    print 'alex: waiting for baozi to be ready'
    while True:
        if event.isSet():
            print u'Thanks...'
            break
        else:
            print u'还尼玛没好啊'
            time.sleep(0.5)  # 这里的time.sleep(0.5)可以换成其它,如干自己的事儿之类


event = threading.Event()

p = threading.Thread(target=producer)
c = threading.Thread(target=consumer)

p.start()
c.start()