# coding:utf-8

import MySQLdb

"""
连接数据库
"""

conn = MySQLdb.connect(host="localhost", user="root", passwd="123", db="PythonStudy", port=3306, charset="utf8")
cur = conn.cursor()
