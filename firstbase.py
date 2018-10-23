#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print(True and True,True and False, True or False,False or False,not False,not True)
#除法运算
print(10/3,10//3,10%3)#整除 地板除取余
#将单个字符变成整数表示
print('A==>',ord('A'),'a==>',ord('a'),'Z==>',ord('Z'),'z==>',ord('z'))
print(ord('庄'),ord('学'),ord('南'))
#将整数变成单个字符
print(chr(24196)+chr(23398)+chr(21335))
print('\u4e2d\u6587')
#对字符串进行encode转码 变成字节 中文不能进行ascii编码 切记切记 英文可以使用ascii和utf-8 两者显示效果一样
# 因为中文编码的范围超过了 ASCII 编码的范围，Python 会报错。
print('中文'.encode('utf-8'))
print('ABC'.encode('ascii'))
print('ABC'.encode('utf-8'))
#将字节变回字符串decode
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(b'ABC'.decode('utf-8'))
print(b'ABC'.decode('ascii'))
#字节数
print(len('中文'),len('ABC'),len(b'ABC'),len(b'\xe4\xb8\xad\xe6\x96\x87'))
#通配符 常用的%d %s 如果你不确定用什么 %s就是万能的
print('hello,%s,wo lisen you have %d$'%('hhah',1000000))
print('%s,\t\t\t\t%d,\t\t\t\t%.2f'%('join',200000,3.1415926))
#如果%是一个普通字符
print('今年的经济增长了%d%%'%(7))

