# -*- coding:utf-8 -*-

import SocketServer


class MyServer(SocketServer.BaseRequestHandler):

    def handle(self):
        # print self.request,self.client_address,self.server
        conn = self.request
        conn.send('May I help U?')
        flag = True
        while flag:
            try:
                data = conn.recv(1024)
                print(data)
                if data == 'exit':
                    flag == False
                elif data == 'view log':
                    conn.send('Wait a sec.')
                elif data.__contains__('weather'):
                    conn.send('Soudesune, totemo atsui desu.')
                elif data.__contains__('mood'):
                    conn.send('Positive views always counts.')
                elif data.__contains__('python'):
                    conn.send('Python is great.')
                else:
                    conn.send('I do not see that.')
            except Exception,e:
                print('连接出故障了：{}'.format(e))
                break
        conn.close()

if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer(('127.0.0.1', 9000), MyServer)
    server.serve_forever()
