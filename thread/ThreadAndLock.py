#!/usr/bin/python
# coding: utf-8

import thread
from time import sleep, ctime


'''
使用thread模块创建线程
'''


def loop0():
    print '开始： ', ctime()
    sleep(4)
    print '结束:  ', ctime()


def loop1():
    print '开始： ', ctime()
    sleep(2)
    print '结束:  ', ctime()


def loop(loop, lock):
    print '开始', loop, ': ', ctime()
    print '结束:  ', ctime()
    lock.release()


def main():
    print '进程开始1：', ctime()
    # 使用start_new_thread()函数创建线程
    thread.start_new_thread(loop0, ())
    thread.start_new_thread(loop1, ())
    sleep(6)
    print '进程结束1: ', ctime()

    print '开始2：', ctime()
    locks = []
    for i in range(0, 5):
        lock = thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in range(0, 5):
        thread.start_new_thread(loop, (i, locks[i]))

        for i in range(0, 5):
            while locks[i].locked():
                pass

    print '结束2：', ctime()

if __name__ == '__main__':
    main()