# -*- coding:utf-8 -*-

from wsgiref.simple_server import make_server
import ex13_conf

def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])

    # 获取用户url
    userUrl = environ['PATH_INFO']

    func = None

    for item in ex11_conf.url:
        if item[0] == userUrl:
            func = item[1]
            break

    if func:
        result = func()
    else:
        result = '404'

    return result

    '''
    if userUrl == '/index/':
        return '<h1>index</h1>'
    elif userUrl == '/login/':
        return '<h1>login</h1>'
    elif userUrl == '/logout/':
        return '<h1>logout</h1>'
    else:
        return '404'
    '''

    return '<h1>Hello, web!</h1>'

if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print "Serving HTTP on port 8000..."
    httpd.serve_forever()