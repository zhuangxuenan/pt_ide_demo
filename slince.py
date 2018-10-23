#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#对list tuple string执行切割操作 前闭后开
L = ['aa','bb','cc','dd','ee','ff','gg']
L2 = L[0:3]#切割前3个元素
print(L2)
#如果是从0开始截取，开头的0还可以省略
print(L[:3])
#如果不是从0开始，开头的数字不能省略
print(L[1:3])
#切片操作同样支持倒数操作 注：倒数第一个元素的索引是-1
print(L[-2:])
F = list(range(40))#生成一个从0到99的数列
print(F)
#取出前10个元素的list的出来
print(F[:10])
#取出第10到第20个的list出来
print(F[10:20])
#把最后10个取出来
print(F[-10:])
#前10个数每两个取一个
print(F[0:10:2],F[:10:2])
#所有的数 每隔5个取一个
print(F[::5])
#原样复制一个list
print(F[:])
#同样的tuple也可以有切片操作 跟list一毛一样的额操作
H = (tuple(range(40)))
print(H)
print(H[:3])
print(H[0:3])
print(H[1:3])
print(H[:10:2])
print(H[::5])
print(H[:])
#字符串可以看成是一种list 同样跟list切片一毛一样的操作 神奇的切片
s = 'abcdefghijklmnopqrstuvwxyz'
print(s[:3])
print(s[0:3])
print(s[1:3])
print(s[:10:2])
print(s[::5])
print(s[:])
