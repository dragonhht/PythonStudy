#! /usr/bin/python
# coding: utf-8

from selenium import webdriver

# 使用Chrome
driver = webdriver.Chrome()

driver.get("https://www.dianping.com/search/category/7/10/p1")

for x in range(0, 10):
    for i in range(0, 2):
        try:
            # 获取a标签class为next的元素(下一页)
            load_more = driver.find_element_by_css_selector('a.next')
            comment = driver.find_element_by_id('shop-all-list')
            contents = comment.find_element_by_tag_name('h4')
            print(contents.text)

            # 点击下一页
            #load_more.click()
        except:
            pass
        
        
