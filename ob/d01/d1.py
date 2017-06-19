# -*- coding:utf-8 -*-
import sys
import time

file_object = open('D:/Exercises/Ex.py/ob/hostInfo.txt')
str_of_all_lines = file_object.read()
file_object.seek(0)  # 位置指针回归，不加则下一行ln8会返回空list
list_of_all_lines = file_object.read().splitlines()
# file_object_w = open('D:/Exercises/Ex.py/ob/hostInfo.txt', 'w+')  # 若取注本行ln9(这时自然ln28要换个头),则ln17无意义而ln18会显示空 ^_^"

# print list_of_all_lines

nowStatus = list_of_all_lines[0][8:]
preName = list_of_all_lines[1][6:]
prePassword = list_of_all_lines[2][10:]

# file_object.seek(0)
# print file_object.read()

if nowStatus == 'lock-on':
    print '本机帐号已锁定,请联系负责人~'
    sys.exit()
else:
    # 倒计时并改写状态
    def countdown(t):
        while t > 0:
            sys.stdout.write('\r帐号锁定时间，还剩 {}s'.format(t))
            t -= 1
            sys.stdout.flush()
            time.sleep(1)
    # open('D:/Exercises/Ex.py/ob/hostInfo.txt', 'w+').write(file_object.read().replace('lock-off', 'lock-on'))  # w/  w+的open会清空文件，故在write后read时就啥都没了，所以内容为空。^_^¦¦¦
        open('D:/Exercises/Ex.py/ob/hostInfo.txt', 'w+').write(str_of_all_lines.replace('lock-off', 'lock-on'))
        sys.exit()

    count = 0
    limit = 4
    while count < limit:
        inputName = raw_input('Plz enter your username: ')
        if inputName != preName:
            print 'Username Error:', count

            if count == limit-1:  # 输错limit次，锁定账号
                countdown(4)

            count += 1
            continue
        else:  # 输对就跳出，进入输密码循环; count变量会传递给下密码循环
            print '1st Else里的count:', count
            break

    # print '???:', count  # 检测count用

    while count < limit:  # 写俩循环是因为放在一个里的话,一旦密码错了就还得回头重新输入用户名>_<¦¦¦
        inputPassword = raw_input('Plz enter your password: ')
        if inputPassword != prePassword:
            print '密码错误:', count

            if count == limit-1:  # 输错limit次，锁定账号
                countdown(4)

            count += 1
            continue
        else:
            print 'Welcome to the Python World!'
            break
