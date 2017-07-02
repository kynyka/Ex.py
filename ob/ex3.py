# -*- coding:utf-8 -*-
# index()|List/Stringy有count(),Dict无
b = ['!', '#', '*', 'Eric', 'alex', 'jack', 'jack', 'a',
     'b', 'c', 'd', 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 4, 2332, 4, 2, 6, 2]
pos = 0
for i in range(b.count(2)):
    if pos == 0:
    	pos = b.index(2)
    else:
     	pos = b.index(2, pos+1)
    print pos
