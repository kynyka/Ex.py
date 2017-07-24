# -*- coding:utf-8 -*-
from utility.sql_helper import MySqlHelper

class Userinfo(object):

    def __init__(self):
        self.__helper = MySqlHelper()

    def Get_One(self, id):
        sql = 'select * from userinfo where id=%s'
        params = (id,)
        return self.__helper.Get_One(sql, params)

    def CheckValidate(self, username, password):
        sql = 'select * from userinfo where username=%s and password=%s'
        params = (username, password)
        return self.__helper.Get_One(sql, params)
