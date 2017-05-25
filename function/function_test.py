# coding:utf-8


# 函数的定义
def add_function(a, b):
    c = a + b
    return c

# 函数的调用
s = add_function(1, 2)
print s


# 给参数一个默认的值，如果调用时为传入值，则为默认值
def test(a, b=3):
    print "a=" + str(a)
    print "b=" + str(b)

test(1, 2)
test(2)


# 当参数个数不确定时 *arg接收到的是一个元组
def func(a, *arg):
    print a
    print arg
    for i in arg:
        print i

func(1, 2, 3, 4, 5, 6, 7, 8)


# 当参数个数不确定时 **arg接收到的是一个字典
def func_2(**args):
    print args

# 注意赋值方式
func_2(x=1, y=2, z="jk", m=45)


# 递归
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

f = fib(5)
print f

