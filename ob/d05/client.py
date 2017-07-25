# -*- coding:utf-8 -*-
# 异步多线程聊天机器人|查阅聊天记录|插入聊天记录
import socket
from model.chatlog import Chatlog

chatlog = Chatlog()


client = socket.socket()
ip_port = ('127.0.0.1',9000)
client.connect(ip_port)
ls = []

while True:
    data = client.recv(1024)
    print data
    ls.append((data,))
    inp = raw_input('client: ')
    client.send(inp)
    ls.append((inp,))
    if inp == 'exit':
        # print ls
        chatlog.Insert_Log(ls)
        break
    if inp == 'view log':
        result = chatlog.View_log()  # 都调用相关表的类了,何必装蒜传表名
        print result # 我就不把查询到的结果也存到表里了

client.close()
