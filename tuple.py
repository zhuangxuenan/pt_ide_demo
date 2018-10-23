#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#tuple是一种不可变的有序列表 因为元素不可变 所以更安全
kk=("ok",12,"boom")
print(kk)
#定义一个空集合
kk2 = ()
print(kk2)
#定义一个只有一个元素的集合、
kk3 = ('fj',)
print(kk3)
#定义一个可变的tuple 虽然tuple不可变 但是他的元素可以是一个可变的list
kk4 = ('ccv','nnm',['12','fh','nj'])
print(kk4)
kk4[2][0]='替换第三个元素中的第一个元素'
kk4[2][2]='替换第三个元素的最后一个元素'
print(kk4)
#替换可变元素
kk4[2][-1]='完全不知道发生了什么'
print(kk4)