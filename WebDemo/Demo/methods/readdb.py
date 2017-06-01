# coding:utf-8

from db import *


# 登录验证
def login(username, password):
    sql = "select * from login where username = " + username + " and password = " + password
    cur.execute(sql)
    lines = cur.fetchall()
    return lines
