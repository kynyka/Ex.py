# -*-coding:utf-8-*-
# aa = 'How long do you want the loop to be printed out? '
# print_num = input(aa)
# count = 0
# while count < 100:
#     if count == print_num:
#         print 'There you got the number:', count
#         choice = raw_input('Do you want to continue the loop?(y/n) ')
#         if choice == 'n':
#             break
#         else:
#             while print_num <= count:  # 第一回合自然是相等的
#                 print_num = input(aa)
#                 # print 'NEW: ', print_num
#                 if print_num <= count:  # 修正输入值大于count时出现打印的bug
#                     print u'已经过了，SX！'
#     else:
#         print 'loop:', count
#     count += 1
# else:  # python里有while else的写法
#     print 'loop:', count


# 某人改为如下来使input只有1次
print_num = 0
count = 0
while count < 100:
    if count == print_num:
        print 'There you got the number:', count
        while print_num <= count:  # 第一回合自然是相等的
            print_num = input('How long do you want the loop to be printed out? ')
            if print_num == 0:
                exit('Exit the Program!')
            if print_num <= count:  # 修正输入值大于count时出现打印的bug
                print u'已经过了，SX！'
    else:
        print 'loop:', count
    count += 1
else:  # python里有while else的写法
    print 'loop:', count