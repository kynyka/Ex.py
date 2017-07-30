# -*- coding:utf-8 -*-
# 线程锁

# import threading
# import time

# num = 0

# def run(n):

#     time.sleep(1)  # 每个线程的sleep时机略有差异;所以可以看到print出来的未必是50个代表线程的数字

#     global num  # 对函数中的局部变量进行全局变量的声明,使之能修改ln7的num
#     lock.acquire()
#     num += 1  # 原本ln15的num与ln7的num是不同的,但ln13的声明使两个同名的变量成为了一个

#     lock.release()
#     time.sleep(0.01)  # py的每次切换线程,每次都是100条指令,但这里sleep了就有了阻塞了,此时是不占cpu空间了,那么就不等它100条了,就切过去了
#     print '%s\n' % num  # 在释放锁之后,对终端就没有独占了,就又开始抢了

# # run('dd')
# # print num

# lock = threading.Lock()

# for i in range(50):
#     t = threading.Thread(target=run, args=(i,))
#     t.start()


import threading
import time

num = 0

def run(n):

    time.sleep(1)

    global num
    samp.acquire()
    time.sleep(0.001)
    num += 1
    print '%s' % num
    samp.release()

samp = threading.BoundedSemaphore(4)  # 信号量,允许同时有几个线程去改数据[那个变量](此处自设数目),可能导致这几个线程获得同样的数据而返回同样的值(结果少了些终端上的输出);1的话效果跟lock一样;mysql的最大同时连接数就是这个

for i in range(200):
    t = threading.Thread(target=run, args=(i,))
    t.start()
