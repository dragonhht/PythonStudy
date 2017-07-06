# coding: utf-8
from SocketServer import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21568
ADDR = (HOST, PORT)


class MyRequestHandler(SRH):

    def handle(self):
        print '连接: ', self.client_address
        self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline()))

tcpServ = TCP(ADDR, MyRequestHandler)
print '等待连接...'
tcpServ.serve_forever()
