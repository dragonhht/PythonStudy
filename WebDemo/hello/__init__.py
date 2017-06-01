# coding:utf-8
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

# 定义服务器端口
define("port", default=8080, help="run", type=int)


class IndexHandler(tornado.web.RequestHandler):

    def data_received(self, chunk):
        pass

    def get(self):
        # 获取URL里的参数,http://localhost:8080/?greeting=hello
        greeting = self.get_argument("greeting", "hello")
        # 向客户端反馈信息
        self.write(greeting + ", welcome")

if __name__ == '__main__':
    tornado.options.parse_command_line()
    # 讲application类实例化, (r"/", IndexHandler) 来自根路径的请求的交给IndexHandler处理
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    # 建立单进程的http服务
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
