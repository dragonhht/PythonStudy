# coding:utf-8

import tornado.ioloop
import tornado.options
import tornado.httpserver

from application import application
from tornado.options import define, options

define("port", default=8080, help="run", type=int)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)

    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
