# -*- coding:utf-8 -*-

def index():
    return 'index_11'

def login():
    return 'login_11'


url = (
    ('/index', index),
    ('/login', login),
    )

print __name__
