# coding:utf-8

import os
import fileinput

# 打开文件
f = open("file/test.txt")
for line in f:
    print line,  # 后面加一个逗号，去掉原来默认增加的\n
f.close()

# 创建文件 （以写方式打开文件）(异常的处理)
try:
    f2 = open("file/test2.txt", "w")
    f2.write("这是一个创建文件的测试")
except Exception, e:
    print "写入错误",  e
finally:
    f2.close()

# 以只读的方式打开文件
f3 = open("file/test2.txt", "r")
for line in f3:
    print "\n" + line
f3.close()

# 以追加模式打开文件
f4 = open("file/test.txt", "a")
f4.write("\n你好呀")
f4.close()

# 使用with打开文件
with open("file/test.txt", "r") as f5:
    print f5.read()

# 查看文件的状态
file_stat = os.stat("file/test.txt")
print file_stat

# 读取大文件时
for line in fileinput.input("file/test.txt"):
    print line,

# 复制图片
# 以二进制模式读取文件
f5 = open("file/3c28af542f2d49f7-da1566425074a021-9c373de8439e52c5d885c8459d285946.jpg", "rb")
f6 = open("file/pic.jpg", "w")
r = f5.read(1)
while r:
    f6.write(r)
    r = f5.read(1)
f5.close()
f6.close()
