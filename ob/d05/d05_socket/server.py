# -*- coding:utf-8 -*-

# import socket

# sk = socket.socket()
# ip_port = ('127.0.0.1',9998)
# sk.bind(ip_port)
# sk.listen(5)  # 等待时候后面可以阻塞几个

# while True:
#     conn,address = sk.accept()
#     conn.send('hello.')
#     flag = True
#     while flag:
#         data = conn.recv(1024)
#         print data
#         print type(data)
#         if data == 'exit':
#             flag == False
#         elif data.__contains__('weather'):
#             conn.send('Soudesune, totemo atsui desu.')
#         elif data.__contains__('mood'):
#             conn.send('Positive views always counts.')
#         elif data.__contains__('life'):
#             conn.send('As for life, how can you avoid mentioning Python?!')
#         elif data.__contains__('python'):
#             conn.send('Python is great.')
#         else:
#             conn.send('I do not see that.')
#     conn.close()

import SocketServer  # Py3中改为小写socketserver


class MyServer(SocketServer.BaseRequestHandler):

    def handle(self):
        # print self.request,self.client_address,self.server
        conn = self.request
        conn.send('Hello')
        flag = True
        while flag:
            try:
                data = conn.recv(1024)
                print(data)
                if data == 'exit':  # https://stackoverflow.com/questions/33003498/typeerror-a-bytes-like-object-is-required-not-str
                    flag == False
                elif data.__contains__('weather'):
                    conn.send('Soudesune, totemo atsui desu.')
                elif data.__contains__('mood'):
                    conn.send('Positive views always counts.')
                elif data.__contains__('life'):
                    conn.send('As for life, how can you avoid mentioning Python?!')
                elif data.__contains__('python'):
                    conn.send('Python is great.')
                else:
                    conn.send('I do not see that.')
            except Exception,e:
                print('连接出故障了：{}'.format(e))
                break
        conn.close()

if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer(('127.0.0.1', 9019), MyServer)
    server.serve_forever()
