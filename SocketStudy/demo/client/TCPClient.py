# coding: utf-8
from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

# 创建客户端套接字
s = socket(AF_INET, SOCK_STREAM)
# 尝试连接服务器
s.connect(ADDR)

# 通信循环
while True:
    # 输入信息
    data = raw_input('> ')
    if not data:
        break
    # 发送信息
    s.send(data)
    # 接受信息
    data = s.recv(BUFSIZ)
    if not data:
        break
    print data

# 关闭客户端套接字
s.close()
