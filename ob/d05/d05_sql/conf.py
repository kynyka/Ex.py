# -*- coding:utf-8 -*-
import pymysql.cursors

connect_dict = dict(host='127.0.0.1',
                    port=3306, # 默认可不写
                    user='root',
                    password='111111',
                    db='08day5',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor)
