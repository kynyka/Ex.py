# -*- coding:utf-8 -*-
# 多进程共享一个终端(屏幕输出)
# library里写明了是a clone of threading.Lock 没啥大用
from multiprocessing import Process, Lock


def f(l, i):
    l.acquire()
    print 'hello world', i
    l.release()

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()
