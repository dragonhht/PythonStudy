# coding:utf-8

# 表示新式类
_metaclass_ = type


class ClassTest:

    # 初始化函数
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


test = ClassTest("你好呀")
s = test.get_name()
print s
