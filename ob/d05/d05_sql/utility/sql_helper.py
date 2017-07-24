# -*- coding:utf-8 -*-
import pymysql.cursors
import conf

class MySqlHelper(object):

    def __init__(self):
        self.__conn_dict = conf.connect_dict

    def Get_Dict(self, sql, params):
        conn = pymysql.connect(**self.__conn_dict)
        try:
            with conn.cursor() as cur:
                cur.execute(sql, params)

            conn.commit()

            data = cur.fetchall()
            return data
        finally:
            conn.close()

    def Get_One(self, sql, params):
        conn = pymysql.connect(**self.__conn_dict)
        try:
            with conn.cursor() as cur:
                cur.execute(sql, params)

            # conn.commit()

            data = cur.fetchone()
            return data
        finally:
            conn.close()
