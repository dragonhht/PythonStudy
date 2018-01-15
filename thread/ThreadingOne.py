#!/usr/bin/python
# coding: utf-8

import threading
from time import sleep, ctime


def loop(num):
    print '线程开始', num, '：', ctime()
    print '线程结束', num, ': ', ctime()


def main():
    for i in range(0, 5):
        # 创建线程
        t = threading.Thread(target=loop, args=(i))
        # 启动线程
        t.start()

if __name__ == '__main__':
    main()
