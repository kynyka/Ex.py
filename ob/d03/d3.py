# -*-coding:utf-8-*-
# 网上银行; 判断时间费了点工夫; 分离得不太好,最好是都返回值而不含嵌套; 负债累积升值不做了
import time
import calendar
import datetime
import sys
import os
import re


def self_check(ex_file_name):  # 程序一运行就首先自检
    if file_exist_or_not(ex_file_name) == 1:  # 有无昨天的明细
        msg = '\n{} —— 重置额度 ——\n  可用额度: {:>9.2f}\n'.format(time.strftime('%Y-%m-%d %H:%M:%S'), ratio_reset)
        log(ex_file_name, msg)  # 重置额度, 但余额自然不会重置
        if today == lastDay:
            os.rename(ex_file_name, bill_name)
            everyday_ratio = initial_ratio  # 每日的消费限额
            balance = get_spec_cnt(bill_name, '帐户余额') if file_exist_or_not(bill_name) == 1 else initial_balance  # 自己在银行的持有资产
        else:
            os.rename(ex_file_name, file_name)
            everyday_ratio = get_spec_cnt(file_name, '可用额度') if file_exist_or_not(file_name) == 1 else initial_ratio  # 每日的消费限额
            balance = get_spec_cnt(file_name, '帐户余额') if file_exist_or_not(file_name) == 1 else initial_balance  # 自己在银行的持有资产
        return [everyday_ratio, balance]
    else:  # 同一日内不重置
        everyday_ratio = get_spec_cnt(file_name, '可用额度') if file_exist_or_not(file_name) == 1 else initial_ratio  # 每日的消费限额
        balance = get_spec_cnt(file_name, '帐户余额') if file_exist_or_not(file_name) == 1 else initial_balance  # 自己在银行的持有资产
        return [everyday_ratio, balance]


def file_exist_or_not(file_name):  # 文件是否存在
    if os.path.exists(file_name):
        return 1
    else:
        return 0


def get_spec_cnt(file_name, srh):  # 根据明细格式, 提取相应信息
    ptn = re.compile(r'(%s\:\s+\-?\d+\.\d{2}\n)' % srh)
    with open(file_name, 'r') as f:
        cnt = f.read()
        fnd = ptn.findall(cnt)
        spec_ln = fnd[len(fnd)-1]
        spec_cnt = float(spec_ln.split(':')[1].replace(' ','').replace('\n',''))  # float会自动过滤到最后一个非零小数
        return spec_cnt


def log(file_name, inf):  # 记录操作明细, 这里不是用logging模块的场合
    with open(file_name, 'a+') as f:  # 不存在则会创建
        f.write(inf)


def payback_or_not(everyday_ratio, balance):  # 是否还款
    print '\n帐户余额: ￥%.2f    资产绝赞NG中...\n' % balance
    case = raw_input('还款请按"y",不还请按"n": ')
    if case == 'y':
        pb = input('还款 ￥')
        balance += pb
        msg = '\n{} —— 还款 ——\n  还款数额: {:>9.2f}\n  帐户余额: {:>9.2f}\n'.format(time.strftime('%Y-%m-%d %H:%M:%S'), pb, balance)
        print msg
        log(file_name, msg)
        shop_withdraw_or_exit(everyday_ratio, balance)
    elif case == 'n':
        print '\n负债中...吃土去'
        sys.exit()
    else:
        payback_or_not(everyday_ratio, balance)


def withdraw_or_not(balance):  # 是否提款
    print '\n当前帐户余额 ￥%.2f' % balance
    case = raw_input('\n哇哦,现持有额度已无法于今日继续购物,但尚能提款。\n要提款请输入"1",要退出请按除"1"以外的任意键: ')
    if case == '1':
        withdraw(balance)
    else:
        sys.exit()


def withdraw(balance):  # 提款,返回帐户余额; 跟每日额度可没半毛钱关系
    money_amount = int(input('请输入提款数额(注意>>提款有5%的手续费): '))  # 向下取整,提款岂带几角几分
    balance -= 1.05 * money_amount  # 资产可为负(算它信用卡?2333)
    msg = '\n{} —— 提款 ——\n  提款数额: {:>9.2f}\n    手续费: {:>9.2f}\n  帐户余额: {:>9.2f}\n'.format(time.strftime('%Y-%m-%d %H:%M:%S'), money_amount, money_amount * 0.05, balance)
    print msg
    log(file_name, msg)
    return balance


def getMonthLastDay(year=None, month=None):  # 获取今年当月的月末号
    year = int(year) if year else datetime.date.today().year
    month = int(month) if month else datetime.date.today().month
    days_span = calendar.monthrange(year, month)[1]
    return days_span


def show_itemlist():  # 若循环字典并按键值格式化打印出来,要控制序号的话,还是得写if判断,还不如直接这样
    print '''
===     All Items for Sell     ===
1. Tablet               ￥%(Tablet)8.2f
2. Bike                 ￥%(Bike)8.2f
3. Watch                ￥%(Watch)8.2f
4. Pudding              ￥%(Pudding)8.2f
5. Spring               ￥%(Spring)8.2f
6. PC                   ￥%(PC)8.2f
''' % shopping_items
    return 1


def get_item_name(item_id):  # 根据输入的商品序号获取其名称; 这写法蠢爆了,然而暂时想不到更好的orz
    if item_id == '1':
        return 'Tablet'
    elif item_id == '2':
        return 'Bike'
    elif item_id == '3':
        return 'Watch'
    elif item_id == '4':
        return 'Pudding'
    elif item_id == '5':
        return 'Spring'
    elif item_id == '6':
        return 'PC'
    else:
        return 0


def get_item_price(item_id):  # 根据输入的商品序号获取其价格
    item_name = get_item_name(item_id)
    if item_name != 0:
        return shopping_items[item_name]  # ==0的坑丢上一级函数解决


def calc_ratio_and_balance(everyday_ratio, balance):  # 计算可用额度及帐户余额
    print '可用额度:%d,帐户余额:%.2f' % (everyday_ratio, balance)
    item_id = raw_input('请输入要购买的商品序号: ')  # 本欲用input,奈防不住找茬的手指不是
    # print '传说中的None/list etc.->',get_item_price(item_id)  # 这个坑是假如输入非商品序号的数字,获取价格函数就会报None(因为我没处理==0时的情况)
    item_price = get_item_price(item_id)
    if item_price is not None:
        if everyday_ratio < min_price:  # 判断此时的额度是否可购买价格最少的商品,不够则进入建议可提款的分支
            withdraw_or_not(balance)
            print '提款完毕,继续吃土!'
            sys.exit()
        everyday_ratio = everyday_ratio - item_price
        balance = balance - item_price
        if everyday_ratio >= 0 and balance >= 0:  # 此时之额度与余额是已经减过的; 买东西时当然不能让资金为负
            msg = '\n{} —— 购物 ——\n  消费金额: {:>9.2f}\n  购入商品: {}\n  可用额度: {:>9.2f}\n  帐户余额: {:>9.2f}\n'.format(time.strftime('%Y-%m-%d %H:%M:%S'), item_price, get_item_name(item_id), everyday_ratio, balance)
            print msg
            log(file_name, msg)
            return [everyday_ratio, balance]
        elif everyday_ratio >= 0 and balance <= 0:  # 空有额度,而余额不够买任何商品 残酷な状况だ
            print '\nWARN: 余额不够买任何商品啦!'
            return payback_or_not(everyday_ratio + item_price, balance + item_price)
        else:
            print '\n请检查自己的可用额度与帐户余额,并重新选购适当的商品!\n'
            return calc_ratio_and_balance(everyday_ratio + item_price, balance + item_price)
    else:
        return calc_ratio_and_balance(everyday_ratio, balance)


def shop_withdraw_or_exit(everyday_ratio, balance):  # 询问购物、提款抑或退出
    if balance <= 0:
        payback_or_not(everyday_ratio, balance)  # 还款接口
    case = raw_input('你是要购物、提款还是退出？\n要购物请输入"1",要提款请按"2",要退出请按除"1""2"以外的任意键: ')
    if case == '1':
        show_itemlist()
        calc_result = calc_ratio_and_balance(everyday_ratio, balance)
        everyday_ratio = calc_result[0]  # 每次消费后计算额度并即时更新可用额度
        balance = calc_result[1]  # 每次消费后计算余额并即时更新帐户余额
        # everyday_ratio = calc_ratio_and_balance(everyday_ratio, balance)[0]  # warn:本行与下行的暴力写法会导致函数执行两次,弃之
        # balance = calc_ratio_and_balance(everyday_ratio, balance)[1]
        # print '>> 赋值后的额度 %d,余额 %d' % (everyday_ratio, balance)
        shop_withdraw_or_exit(everyday_ratio, balance)
    elif case == '2':
        print '\n当前帐户余额 ￥%.2f' % balance
        balance = withdraw(balance)
        shop_withdraw_or_exit(everyday_ratio, balance)
    else:
        sys.exit()


ratio_reset = 15000  # 每次重置的额度值
initial_ratio = 15000
initial_balance = 20000
# everyday_ratio = get_spec_cnt('可用额度') if file_exist_or_not(file_name) == 1 else 15000  # 每日的消费限额
# balance = get_spec_cnt('帐户余额') if file_exist_or_not(file_name) == 1 else 20000  # 自己在银行的持有资产;2w只第1次有用

year = time.localtime()[0]  # 本年
month = time.localtime()[1]  # 本月
today = time.localtime()[2]  # 获取今天的日子号
lastDay = getMonthLastDay()  # 替代只判断是否到了每月30号的条件,改成这个好了

file_name = 'D:/Exercises/Ex.py/ob/d03/tmp-{}.txt'.format(time.strftime('%Y-%m-%d',time.localtime()))  # 当天文件名
yesterday_ymd = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')
ex_file_name = 'D:/Exercises/Ex.py/ob/d03/tmp-{}.txt'.format(yesterday_ymd)
bill_name = 'D:/Exercises/Ex.py/ob/d03/bill-{}-{:02}-{:02}.txt'.format(year, month, lastDay)

shopping_items = {'Tablet':4200, 'Bike':500, 'Watch':2000, 'Pudding':30, 'Spring':10, 'PC':6000}
min_price = min(shopping_items.itervalues())  # 后面将余额与最少价值物品比较用


if __name__ == "__main__":
    check_out = self_check(ex_file_name)
    everyday_ratio = check_out[0]
    balance = check_out[1]
    while (everyday_ratio >= 0):
        shop_withdraw_or_exit(everyday_ratio, balance)
