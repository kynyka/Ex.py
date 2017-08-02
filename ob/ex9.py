# -*- coding:utf-8 -*-
# 两种写法

# from multiprocessing import Pool
# import time

# def f(x):
#   # time.sleep(0.5)
#   print x*x
#   return x*x

# if __name__ == '__main__':
#   p = Pool(5)
#   print(p.map(f,range(50)))


from multiprocessing import Process
import os


def info(title):
    print title
    print 'module name:', __name__
    if hasattr(os, 'getppid'):  # only availabe on *nix
        print 'parent process:', os.getppid()
    print 'process id:', os.getpid()


def f(name):
    info('function f')
    print 'hello', name


if __name__ == '__main__':
    info('main line')
    print '---------------'
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
