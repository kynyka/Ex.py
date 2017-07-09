# -*- coding:utf-8 -*-
# trolley
items = '''
=== All Items for Sell ===
Tablet   $4800
Bike     $2000
Lamy     $500
'''
print items
moneyIGet = input('Enter the amount of your current money: ')
print '你当前持有$%s' % moneyIGet

itemValue = [4800, 2000, 500]  # 还没用到字典
delta = moneyIGet
while delta > min(itemValue):
    itemIBuy = raw_input('What would you buy? ')
    if itemIBuy == 'Tablet':
        if delta - itemValue[0] < 0:
            print '当前所持金钱不足以购买本商品...'
        else:
            delta = delta - itemValue[0]
            print '你还剩$%s' % delta
            if delta < min(itemValue):
                print 'Your current money is NOT ENOUGH for any item!'
                break
    elif itemIBuy == 'Bike':
        if delta - itemValue[1] < 0:
            print '当前所持金钱不足以购买本商品...'
        else:
            delta = delta - itemValue[1]
            print '你还剩$%s' % delta
            if delta < min(itemValue):
                print 'Your current money is NOT ENOUGH for any item!'
                break
    elif itemIBuy == 'Lamy':
        if delta - itemValue[2] < 0:
            print '当前所持金钱不足以购买本商品...'
        else:
            delta = delta - itemValue[2]
            print '你还剩$%s' % delta
            if delta < min(itemValue):
                print 'Your current money is NOT ENOUGH for any item!'
                break
    else:
        print '这里没有这种商品哦!'
else:
    print '钱不够哩,继续吃土!'
