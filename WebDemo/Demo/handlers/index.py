# coding:utf-8

import tornado.web
import methods.readdb as mrd


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        # 向用户反馈网页
        self.render("login.html")

    # 处理数据,post提交数据
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        lines = mrd.login(username, password)
        if lines != ():
            self.render("success.html")
        self.render("login.html")
