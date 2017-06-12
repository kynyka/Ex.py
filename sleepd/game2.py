# -*- coding:utf-8 -*-
# def Misaka(action):
#   if action == "say":
#       print "Misaka:..."
#   if action == "attack":
#       print "Railgun!"

# Misaka('say')
# Misaka('attack') #以上为面向过程方式，以下改为面向对象


class Misaka(object):  # 创建类

    def __init__(self):  # 创建属性
        self.name = 'Misaka'

    def say(self, words):  # 创建方法,第一个参数self几乎不去动它
        print "{1}: {0}".format(words, self.name)

    def attack(self):
        print u"超电磁炮!"


# misaka = Misaka()  # 实例化
# misaka.say('びりびりじゃねの')
# misaka.attack()
class Sister(Misaka):  # 类的继承
    def __init__(self, _id):
        self.name = 'Sister'
        self.id = _id

    def attack(self):
        print u"番号{0}: 自動小銃！".format(self.id)


sisters = []

for i in range(5):
    sisters.append(Sister(i))

print len(sisters)

misaka = Misaka()
sister = Sister(10)

misaka.say('...')
sister.attack()

print sisters
