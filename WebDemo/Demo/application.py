# coding:utf-8

from url import url
import tornado.web
import os

# 约定模板与静态文件的路径
settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    statics_path=os.path.join(os.path.dirname(__file__), "statics")
)

# 请求处理集合
application = tornado.web.Application(
    handlers=url,
    **settings
)
