# -*- coding:utf-8 -*-
import random

number = random.randint(1, 10)
guess_count = 0
game_not_end = True

while game_not_end:
    guess_count = guess_count + 1
    # raw_input返回的是字符串
    player_input = int(raw_input("input a number({0}): ".format(guess_count)))
    if number == player_input:
        print "you win!"
        game_not_end = False
        # break #中断并不代表退出程序；这里循环后无其它语句，故中断了即退出了
    elif player_input > number:
        print "bigger"
    else:
        print "smaller"  # 二叉树来猜
