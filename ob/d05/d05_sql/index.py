# -*- coding:utf-8 -*-
from model.userinfo import Userinfo

def main():

    user = raw_input('username:')
    pwd = raw_input('password:')
    userinfo = Userinfo()
    result = userinfo.CheckValidate(user, pwd)
    print result




if __name__ == '__main__':
    main()