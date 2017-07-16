# -*- coding:utf-8 -*-

class Chara(object):
    def __init__(self, name, inlove, partner, Fasle):
        self.name = name
        self.inlove = inlove  # bool是否有男女朋友
        self.partner = partner
        self.__hadSex = Fasle

    @property
    def laid(self):
        return self.__hadSex

    @laid.setter
    def laid(self, __hadSex):
        self.__hadSex = __hadSex

    def state(self, name, inlove, partner):
        if inlove == 1 and partner is not None:
            return u'{}与{}正男女朋友中'.format(name, partner)
        elif inlove == 0 and partner is not None:
            return u'此时的{}已然绿茶'.format(name)
        else:
            return u'{}也算是孤家寡人了'.format(name)


class TallRichNice(Chara):
    def __init__(self):
        # Chara.__init__(self, name, inlove, partner, Fasle)
        pass

    def socialStatus(self, name, villaCount):
        if villaCount >= 1:
            return [1, u'拥有{}座别墅的高富帅{}!'.format(villaCount, name)]
        else:
            return [0, u'没有别墅的屌丝{}!!'.format(name)]
