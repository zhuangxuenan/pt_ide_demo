#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


def fuction_abs(x):
    # 类型检查
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x > 0:
        return x
    elif x < 0:
        return -x
    else:  # pass可以作为占位符 当没有想好这一块代码怎么写的时候可以写一个pass进去
        pass


# 函数有多个返回值 多个返回值的情况下实际上是个tuple 也就是一个不可变数组
# 因为tuple不可变 所以仍然是一个返回值
def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


def move2(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return [nx, ny]


def move3(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return (nx, ny)


# 位置参数
# 调用函数时，传入的两个值按照位置顺序依次赋值
# 默认参数
# 默认参数可以简化函数的调用 在位置参数没有传的时候 避免报错 降低调用函数的难度
# 一是必选参数在前，默认参数在后
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数
# 默认参数必须指向不变对象！
def power(x, n=2):
    s = 1
    while (n > 0):
        n -= 1;
        s *= x
    return s


def enroll(name, genger, age=6, city='BeiJing'):
    print('name:', name, 'genger:', genger, 'age:', age, 'city:', city)


def add_end(L=[]):
    L.append('END')
    return L


def add_end2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


def calc(numbers):
    sum = 0
    for n in numbers:
        sum += (n * n)
    return sum


# 可变参数
# 定义可变参数和定义一个 list 或 tuple 参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数 numbers 接收到的是一个 tuple，因此，函数
# 代码完全不变。但是，调用该函数时，可以传入任意个参数，包括 0 个参数
def calc2(*numbers):
    sum = 0
    for n in numbers:
        print('ffffffffffffffffffffffff',type(n))
        if isinstance(n,int):
            sum += (n * n)
    return sum


# 关键字参数
# 而关键字参数允许你传入 0 个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个 dict
# 和可变参数类似，也可以先组装出一个 dict，然后，把该 dict 转换为关键字参数传进去 在传参的时候前边加**
# **extra 表示把 extra 这个 dict 的所有 key-value 用关键字参数传入到函
# 数的 **kw 参数， kw 将获得一个 dict，注意 kw 获得的 dict 是 extra 的一份
# 拷贝，对 kw 的改动不会影响到函数外的 extra
# >>> extra = {'city': 'Beijing', 'job': 'Engineer'}
# >>> person('Jack', 24, **extra)
# name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
def enoll2(name, genger, **kw):
    print('name:', name, "genger:", genger, 'kw:', kw)


# 命名关键字参数
# 用途：限制关键字参数的名字
# 这样的话如果传入一个没有定义过的参数
# 就会报错got an unexpected keyword argument 'xx'
# 也就是这个xx参数没有定义
# 并且跟关键字参数不同 关键字参数定义了可以不传，但是命名关键字参数如果定义了不传就会报错
# 如下xx和yy两个参数没有被定义
# missing 2 required keyword-only arguments: 'xx' and 'yy'
# 使用命名关键字参数时，要特别注意， * 不是参数，而是特殊分隔符。
# 如果缺少 * ，Python 解释器将无法识别位置参数和命名关键字参数
def person(name, age, *, city, job):
    print('name:', name, 'age:', age, 'city:', city, 'job:', job)


# 命名关键字参数可以有缺省值，从而简化调用
def person2(name, age, *, city='Beijing', job):
    print('name:', name, 'age:', age, 'city:', city, 'job:', job)


# TODO 在 Python 中定义函数，可以用必选参数、默认参数、可变参数、关键
# TODO 字参数和命名关键字参数，这 5 种参数都可以组合使用，除了可变参数
# TODO 无法和命名关键字参数混合
# TODO 必选参数在前，默认参数在后 （*可变参数 **关键字参数可以一块用,可变参数不能和命名关键字参数一块用）
# def f1(a, b, c=0, *args, **kw):√正确
#   print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
# def f2(a, b, c=0, *, d, **kw):√正确
#   print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
# def f2(a, b, c=0, *, d, *kw):×错误
#   print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
def f1(a, b, c=0, *args, **kw):  # 必选参数 默认参数 可变参数 关键字参数
    print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)


def f2(a, b, c=0, *, d=0, **kw):  # 必选参数 默认参数 ，命名关键字参数 关键字参数
    print('a=', a, 'b=', b, 'd=', d, 'kw=', kw)


# TODO
# TODO 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
# TODO 要注意定义可变参数和关键字参数的语法：
# TODO *args 是可变参数，args 接收的是一个 tuple；
# TODO **kw 是关键字参数，kw 接收的是一个 dict。
# TODO 以及调用函数时如何传入可变参数和关键字参数的语法：
# TODO 可变参数既可以直接传入： func(1, 2, 3) ，又可以先组装 list 或 tuple，
# TODO 再通过 *args 传入： func(*(1, 2, 3)) ；

# 递归函数

# 使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈
# （stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层
# 栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，
# 所以，递归调用的次数过多，会导致栈溢出。
# 解决递归调用栈溢出的方法是通过 尾递归优化，事实上尾递归和循环的
# 效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return 语句不
# 能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递
# 归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
    # 代码不是越多越好，而是越少越好。代码不是越复杂越好，而是越简单越好。
