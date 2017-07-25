# -*- coding:utf-8 -*-
from utility.sql_helper import MySqlHelper

class Chatlog(object): # Table chatlog

    def __init__(self):
        self.__helper = MySqlHelper()

    def View_log(self):
        sql = 'SELECT * FROM chatlog'
        params = ()
        return self.__helper.Get_Dict(sql, params)

    def Insert_Log(self, ls):
        sql = 'INSERT INTO chatlog (cnt) VALUES (%s)' # postvalues parentheses!
        params = ls
        return self.__helper.Insert_List(sql, params)
