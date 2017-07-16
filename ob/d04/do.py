# -*- coding:utf-8 -*-
import sys
import time

class Do(object):
    def __init__(self, name1, name2, name3, select):
        self.name1 = name1  # Liz
        self.name2 = name2  # John
        self.name3 = name3  # Peter
        self.select = select  # 个人之选择

    def stepOut1st(self, name2, select):
        if select == 1: # 当网管
            print u'\n于是{}跑去当了月薪3K的小网管,挣钱供女友上学.'.format(name2)
            # pass # 因为要输入数字,故没法嵌套只能顺序
        else:
            print u'\n{}认命了,心想着上天对我如此不公,怀着愤懑的心情以及对女友的无限遗憾与不舍,回到了老家.然闻其终死惟日日抱怨不歇而无他所作也.'.format(name2)
            sys.exit()

    def partnerChoice(self, name1, name2, name3, select2):
        if select2[0] == 1:  # 选择Peter
            print u'\n现实的{}傍上了{},爽快地抛弃了{}.\n'.format(name1, name3, name2)
        else:
            print u'\n然天不遂人愿,{}因过劳而亡,{}亦于三月后,不堪悲痛而逝.\n'.format(name2, name1)
            sys.exit()



    def storyTell1st(self):#, name1, name2, name3
        print u'Liz与John原为高中情侣,Liz高考考上了XX大学,John则落榜.于是John面临了留下与回老家两种选择.\n'
        select = input('Enter"1" if "Stay In"; Enter "non 1" number if "Go Home": ')
        self.stepOut1st(self.name2, select)  # 不写self则在main中成了global变量
        print u'\n光阴荏苒,女友毕业,此时的她遇到了她的上司————'

    def storyTell2nd(self, select2, scorn): #, name1, name2, name3
        self.partnerChoice(self.name1, self.name2, self.name3, select2)
        print u'\n{}的耳边犹回荡着{}的嘲讽声: {}.\n那对狗男女就那样开始了苟且的生活.却不知{}已暗暗发誓,定要让自己强大到足以湮没周围对自己的质疑声!\n'.format(self.name2, self.name1, scorn[1], self.name2)

    def storyTell3rd(self, exState):
        for x in xrange(1,6):
            sys.stdout.write(u'\r{}年过去了...'.format(x))
            sys.stdout.flush()
            time.sleep(1)
        print u'\n\n{}这几年来发奋学习,日夜苦读Python,技术终有大成,如今已是周围人艳羡、月薪50K的某一线大厂IT总监!某日路上偶遇{},彼大吐苦水,欲求复合云云.\n{}斟酌一番,了解到这个情况: {}\n'.format(self.name2, self.name1, self.name2, exState)
        select3 = input('“复合”填入数字“1”; “滚粗”填入任意“非1”的数字: '.decode('utf-8').encode('cp936'))
        if select3 == 1:
            print u'\n就是这么任性～ 纵然初恋成绿茶,我待初恋心不变.  ——Fin——'
        else:
            print u'\nあばよ、悪女！  ——Fin——'