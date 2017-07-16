# -*- coding:utf-8 -*-
# 讲个故事|storyTell1st~3rd其实可以合并成一个;如此仅供自己参考传参方式
from character import Chara
from character import TallRichNice  # 即使是子类,不导入也会报 name 'xxx' is not defined的错
from do import Do
import sys

if __name__ == '__main__':
    d1 = Do('Liz', 'John', 'Peter', None)
    c1 = TallRichNice()
    # c2 = Chara('Liz', 1, 'John', False)  # 自定义Liz的状态
    # c3 = Chara('Liz', 1, 'Peter', True)  # 同上
    c4 = Chara('Liz', 0, 'Peter', True)
    select2 = c1.socialStatus('Peter', 5)
    scorn = c1.socialStatus('John', 0)
    exState = c4.state('Liz', 0, 'Peter')

    d1.storyTell1st()
    d1.storyTell2nd(select2, scorn)
    d1.storyTell3rd(exState)
