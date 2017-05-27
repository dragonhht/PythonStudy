# coding:utf-8

# 表示新式类
_metaclass_ = type


class ClassTest:

    # 初始化函数
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    # 私有
    def _test_1_(self):
        pass

    # 私有
    def __test_2(self):
        pass

    # 类方法
    @classmethod
    def class_method(cls):
        pass

    # 静态方法
    @staticmethod
    def static_method():
        pass


if __name__ == '__main__':
    test = ClassTest("你好呀")
    s = test.get_name()
    print s


