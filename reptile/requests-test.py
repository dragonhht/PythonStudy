#! /usr/bin/python
# coding: utf-8

"""
使用Requests，抓取静态页面
"""

import requests
from bs4 import BeautifulSoup


link = 'http://www.santostang.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

# 获取网页源代码
r = requests.get(link, headers, timeout = 1000)
# 获取返回信息
print('status：%d, encoding: %s' %(r.status_code, r.encoding), end='\n')
# 相应体
print(r.content)
# 相应内容
print(r.text)
# requests内置的JSON解码器
# r.json()

# 解析, 使用lxml HTML解析器
soup = BeautifulSoup(r.text, "lxml")
# 查找
title = soup.find("h1", class_="post-title").a.text.strip()

print(title)

# with open('title.txt', 'a+') as f:
#     f.write(title)
#     f.close()
