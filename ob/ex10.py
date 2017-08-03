# -*- coding:utf-8 -*-
# library: 16.6.1.4Shareing state between processes
# 进程间通讯 1.Queue类 2.Value 和 Array (这俩能修改原始进程里的东西) 只能处理数字和列表  3.Manager支持任意类型对象

# 这个Queue不是那个单独的Queue模块,而是multiprocessing里的Queue类
from multiprocessing import Process, Queue
### import Queue as Q2


def f(q, n):
    q.put([n, 'hello'])

if __name__ == '__main__':
    q = Queue()
    ### q = Q2.Queue()
    q.put('ddd')
    for i in range(5):
        p = Process(target=f, args=(q, i))
        p.start()
    while True:
        print q.get()  # 原本5次的进程实际只输出了1次|但Q2那个q,被克隆5份后就跟原始的q没关系了,所以就取不到数据了,于是阻塞






# ----↓----默认无法通信的演示----↓---- windows上报错
# from multiprocessing import Process
# import threading

# def run(inof_list, n):
#   info_list.append(n)
#   print info_list

# info = []
# for i in range(10):
#   p = Process(target=run, args=[info,i])
#   p.start()

# print '-------threading----------'
# for i in range(10):
#   p = threading.Threading(target=run, args=[info,i])
#   p.start()

# ----↑----





# ----↓---- Value Array 用法
# from multiprocessing import Process, Value, Array

# def f(n, a, raw):
#     n.value = 3.1415927
#     for i in range(len(a)):
#         a[i] = -a[i]
#     raw.append(9999)
#     print raw

# if __name__ == '__main__':
#     num = Value('d', 0.0)
#     arr = Array('i', range(10))
#     raw_list =range(10)
#     print num.value
#     print arr[:]  # 不加冒号打印的是对象而非列表

#     p = Process(target=f, args=(num, arr, raw_list))
#     p.start()
#     p.join()

#     print num.value  # 克隆后
#     print arr[:]  # 克隆后
#     print raw_list
# ----↑----


# ----↓---- Manager 用法
# from multiprocessing import Process, Manager

# def f(d, l):
#     d[1] = '1'
#     d['2'] = 2
#     d[0.25] = None
#     l.reverse()

# if __name__ == '__main__':
#     manager = Manager()

#     d = manager.dict()
#     l = manager.list(range(10))

#     p = Process(target=f, args=(d, l))
#     p.start()
#     p.join()

#     print d
#     print l
# ----↑----