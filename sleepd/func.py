# -*- coding:utf-8 -*-
# def plus(x):
#     x += 1
#     return x


# b = 110

# print plus(b)

# import time
# import sys

# def countdown(t):
#     while t > 0:
#         sys.stdout.write('\r帐号锁定时间，还剩 {}s'.format(t))
#         t -= 1
#         sys.stdout.flush()
#         time.sleep(1)

# countdown(4)
# sys.exit()
# a = [1,'2dd',3,4]
# for k,v in enumerate(a):
#   print k,v

# def progress(text):
#     bar_length = 20
#     for percent in xrange(0, 101):
#         hashes = '#' * int(percent/100.0 * bar_length)
#         spaces = ' ' * (bar_length - len(hashes))
#         sys.stdout.write('\r%s: [%s] %d%%' % (text, hashes + spaces, percent))
#         sys.stdout.flush()
#         time.sleep(0.1)
# progress('Loading')

import math


def prime(n):
    if n <= 1:
        return 0
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return 0
    # print n
    return 1

if __name__ == "__main__":
    n = 38  # 因为在repl里直接运行来看，故此处直接赋值而不是拖到cmd里打参数了
    x = [i for i in range(2, n + 1)]
    print x
    # for i in range(2,n+1):
    #     if prime(i):
    #         print i
    # map(prime, x)
    print filter(prime, x)

url = (
    ('/index', 1),
    ('/login', 2),
    )

for i in url:
    print i


