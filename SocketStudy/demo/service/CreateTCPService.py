# coding: utf-8
from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

# 创建服务器套接字
s = socket(AF_INET, SOCK_STREAM)
# 套接字与地址绑定
s.bind(ADDR)
# 监听连接
s.listen(5)
# 服务器无限循环
while True:
    print '等待连接...'
    # 接受客户端连接
    tcpCliSock, addr = s.accept()
    print '... 连接: ', addr

    # 通信循环
    while True:
        # 接受消息
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        # 发送消息
        tcpCliSock.send('[%s] %s' % (ctime(), data))

    # 关闭客户端套接字
    tcpCliSock.close()
