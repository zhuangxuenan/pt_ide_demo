#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterable
#Python的迭代跟java不同 java的迭代必须要有下标才可以迭代
#但是Python只有是可迭代对象无论有没有下标，都可以迭代
#比如list,tuple,dict,set,甚至字符串都可以
#比如dict
dict_f = {'aa':12,'bb':13,'cc':14}
gg = 2131231
list_f = [213,3213,3213,32432,432542]
#key迭代
for key in dict_f:#因为dict是无需的 所以每次迭代的结果可能不一样
    print(key)
#value迭代
for value in dict_f.values():
    print(value)
#同时迭代key和value
for k,v in dict_f.items():
    print(k,v)
#字符串的迭代
s = 'abcdef'
for s_v in s:
    print(s_v)
#判断一个对象是否是可迭代对象
#通过 collections 模块的 Iterable 类型判断
if(isinstance(dict_f,Iterable)):#dict可迭代
    for k, v in dict_f.items():
        print(k, v)
if(isinstance(gg,Iterable)):#整数不可迭代
    for fv in gg:
        print(fv)
if(isinstance(list_f,Iterable)):#list可迭代
    for fv in list_f:
        print(fv)
if(isinstance(s,Iterable)):#字符串可迭代
    for fv in s:
        print(fv)
#Python实现类似于java那样的下标循环
#Python 内置的 enumerate 函数可以把一个 list 变成索引-元素对，这样就
#可以在 for 循环中同时迭代索引和元素本身
for i,value in enumerate(list_f):
    print(i,value)
#同时引用两个变量
for x,y in [(1231,3213),(3213,3243),(3214,345)]:
    print(x,y)
#列表生成式
#列表生成式即 List Comprehensions，是 Python 内置的非常简单却强大的
#可以用来创建 list 的生成式
#写列表生成式时，把要生成的元素 x*x放到前面,后面跟 for 循环，就可以把list创建出来
L = [x*x for x in range(10)]
print(L)
#for 循环后面还可以加上 if 判断
L2 = [x*x for x in range(10) if x%2==0]
print(L2)
#双层循环 实现全排列
L3 = [m+n for m in 'ABC' for n in 'XYZ']
print(L3)
#把一个list中的字符串大写变小写
L4 = ['Hello',16, 'World', 'IBM', 'Apple']
L5 = [s.lower() for s in L4 if isinstance(s,str)]
print(L5)
L6 = [s.lower() if isinstance(s,str)else s for s in L4]#三目运算符
print(L6)
#python三目运算符
a=3
b=4
c=5
print(a if(a>b) else b)

d = (a if (a>b) else b)
print(d if(d>c) else c)
#生成器generator 一边循环一边计算的机制 节省内存
#<generator object <genexpr> at 0x0000024640306EB8>
g = (x*x for x in range(10))
print(g)
for n in g:
    print(n)
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
print('----------------------------')
fib(10)
print('----------------------------')
#如果一个函数定义中包含 yield 关键字，那么这个函数就不再是一个普通函数，而是一个 generator
#但是用 for 循环调用 generator 时，发现拿不到 generator 的 return 语句
#的返回值。如果想要拿到返回值，必须捕获 StopIteration 错误，返回值
#包含在 StopIteration 的 value 中
#generator 函数的“调用”实际返回一个 generator 对象：
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
def fib2(max):
    #try:
        n, a, b = 0, 0, 1
        while n < max:
            yield b
            a, b = b, a + b
            n = n + 1
        return 'done'
    #except StopIteration as e:
    #   print(e.value)
f = fib2(10)
print(f)
while True:
    try:
        hn = next(f)
        print('f:',hn)
    except StopIteration as e:
        print("打印完了")
        print('Generator return value:',e.value)
        break
for bb in f:
    print(bb)

