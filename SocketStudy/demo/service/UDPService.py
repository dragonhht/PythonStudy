# coding: utf-8
from socket import *

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

# 创建服务器套接字
s = socket(AF_INET, SOCK_DGRAM)
# 绑定服务器套接字
s.bind(ADDR)

# 服务器无限循环
while True:
    print '等待...'
    # 接受信息
    data, addr = s.recvfrom(BUFSIZ)
    # 发送信息
    s.sendto('UDP连接: ' , addr)
    print 'received:', addr
