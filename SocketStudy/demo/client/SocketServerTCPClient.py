# coding: utf-8
from socket import *

HOST = 'localhost'
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(ADDR)
    data = raw_input('> ')
    if not data:
        break
    s.send('%s\r\n' % data)
    data = s.recv(BUFSIZ)
    if not data:
        break
    print data.strip()
    s.close()
