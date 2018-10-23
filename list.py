#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#list是一种有序的集合 可以随时添加和删除其中的元素
#元素可以是不同的数据类型 也可以是一个集合
kk=["action1","action2","action3","action4","action5"]
print(kk)
#得到集合的元素个数
print(len(kk))
#用索引的方式拿到集合的每个元素
print(kk[0],kk[1],kk[2],kk[3],kk[4])
#得到集合的最后一个颜色值
print(kk[-1])
#在集合后边追加一个元素
kk.append("我是后来增加的")
print(kk)
#在某个位置添加一个元素
kk.insert(3,"在第四个位置加一个鬼东西")
print(kk)
#将list调转过来
kk.reverse()
print(kk)
#删除某个位置的元素pop(index) 删除最后一个元素pop()或者pop(-1)
kk.pop()
print(kk)
#替换某个位置的元素
kk[1]="我替换了这个位置的一个元素"
print(kk)
