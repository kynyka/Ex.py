# -*- coding:utf-8 -*-

from wsgiref.simple_server import make_server
from Controller.Account import *
from Controller.Admin import *


url = (
    ('/index', Index),
    ('/manage', Index),
    ('/login', Login)
)


def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])

    # 获取用户url
    userUrl = environ['PATH_INFO']

    func = None
    for item in url:
        if item[0] == userUrl:
            func = item[1]
            break
    if func:
        result = func()
    else:
        result = '404'
    return result

if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print "Serving HTTP on port 8000..."
    httpd.serve_forever()