#-*- coding:utf-8 -*-
import random


def roll(n):
    number = [] # 创建列表
    for i in range(n):
        randnum = random.randint(1, 6)
        number.append(randnum)

    return number

com = {'hp':3} #创建字典(它是无序的,但查找比列表快)
player = {'hp':10} #同上

while 1:
    com['roll_result'] = roll(4) #字典不用像列表那样用append从后面添加进来
    player['roll_result'] = roll(5)

    print com, player

    if sum(com['roll_result']) > sum(com['roll_result']):  # 对列表内值求和，不用sum，则只对第1个比较大小
        print "COM win"
        player['hp'] -= 1
    else:
        print "PLAYER win"
        com['hp'] -= 1

    if com['hp'] <= 0 or player['hp'] <= 0:
        break
