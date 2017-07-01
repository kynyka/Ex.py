# -*- coding:utf-8 -*-
import sys
import re


def func(m):
    return '\033[32m' + m.group() + '\033[0m'


f = open('D:/Exercises/Ex.py/ob/search4d2.txt')
f_str = f.read()

while 1:
    srh = raw_input('''-> 若要退出查找程序,请输入":wq" <-
(❤ฺ￫∀￩) おつかれ♫♬ (￫∀￩❤ฺ) キーワードに入力します: ''')
    if srh != ':wq':
        ptn = re.compile(r'%s' % srh)
        amount = ptn.findall(f_str)
        print u'找到%d个匹配' % len(amount)
        f.seek(0)
        amend = ptn.sub(func, f_str)
        print amend
    else:
        sys.exit()
