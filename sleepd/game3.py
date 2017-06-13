# -*- coding:utf-8 -*-
import random


class Skill(object):
    def __init__(self, name, cd, atk, hit):
        self.name = name
        self.maxCD = cd
        self.cd = cd
        self.atk = atk
        self.hit = hit

    def checkCD(self):
        if self.cd > 0:
            self.cd -= 1


class Character(object):
    def __init__(self, name, skills, hp):
        self.name = name
        self.skills = skills
        self.hp = hp

    def attack(self, target):
        skill_to_use = None
        for skill in self.skills:
            skill.checkCD()
            if skill.cd == 0 and not skill_to_use:
                skill_to_use = skill

        if skill_to_use:
            print u"{0}使用{1}技能攻击{2},".format(self.name, skill_to_use.name, target.name),  # 这里加逗号能连起下一行print
            # 判断是否命中
            if random.randint(1, 100) < skill_to_use.hit:
                print u"造成{0}点伤害".format(skill_to_use.atk)
                target.hp -= skill_to_use.atk
            else:
                print u"但是未命中。"

            skill_to_use.cd = skill_to_use.maxCD


class Battle(object):
    def __init__(self, char1, char2):
        self.char1 = char1
        self.char2 = char2

    def start(self):
        battleNotEnd = True
        while battleNotEnd:
            self.char1.attack(self.char2)
            battleNotEnd = self.isBattleNotEnd()
            self.char2.attack(self.char1)
            battleNotEnd = self.isBattleNotEnd()

        if self.char1.hp <= 0:
            loser = self.char1
        else:
            loser = self.char2

        print u"{0}战败。".format(loser.name)

    def isBattleNotEnd(self):
        if self.char1.hp <= 0 or self.char2.hp <= 0:
            return False
        else:
            return True


if __name__ == '__main__':
    skill1 = Skill(u'超电磁炮', 3, 100, 40)
    skill2 = Skill(u'电击', 1, 30, 70)
    misaka = Character(u'炮姐', [skill1, skill2], 110)

    skill3 = Skill(u'激光', 1, 50, 60)
    mugino = Character(u'麦姐', [skill3], 90)

    battle = Battle(mugino, misaka)
    battle.start()
