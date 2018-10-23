#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

from fuction import fuction_abs, move2, move, move3, power, enroll, add_end, add_end2
from fuction import calc,calc2,enoll2,person,person2,f1,f2,fact
#python为大家封装了一些函数 可以直接调用
print(abs(100),abs(-100))#取一个数字的绝对值
print(max(11,55,55,22,45,788,9777))#取最大值出来
#类型转换函数
print(int('34'),str(24),float('13.13'),float('13'),bool(0),bool(1))
#1.当对数字使用bool函数时，0返回假(False),任何其他值都返回真。
#2.当对字符串使用bool函数时，对于没有值的字符串(也就是None或者空字符串)返回False，否则返回True。
print(fuction_abs(15))
print(fuction_abs(-15))
print(fuction_abs(0))
#多个返回值的实际上是个tuple 也就是说是个不可变数组
p = move(100,100,60,math.pi/6)
print(p)
x,y = move(100,100,60,math.pi/6)
print(x,y)
name = move2(100,100,60,math.pi/6)
print(name)
tgg = move3(100,100,60,math.pi/6)
print(tgg)
print(power(5,2),power(5,5),power(5))
enroll('Tom','男')
enroll('Join','男',7)
print(add_end())#['END']
print(add_end())#['END', 'END'] 默认参数必须指向不可变对象
print(add_end2())#[]
print(add_end2())#['END'] 默认参数必须指向不可变对象
print('传入list打印结果：',calc([1,3,4]))
print('传入tuple打印结果：',calc((1,3,4)))
print('可变参数打印结果：',calc2(1,3,4))
print('可变参数打印结果：',calc2(*(1,3,4)))#传入一个tuple
print('关键字参数打印结果：')
enoll2('Toamae','F',city='BeiJing',job = 'chuiniu')
enoll2('Toamae','F',**{'city':'BeiJing','job':'chuiniu'})
dict_c = {'first':'第一个','second':'第二个','third':'第三个'}
enoll2('花生油','F',**dict_c)#先组装一个dict 然后传入 但是前边要加**
person('死啦死啦',36,city='BeiJing',job='吹牛逼')#命名关键字参数
person2('死啦死啦',36,job='吹牛逼')#命名关键字参数
#只传入必选参数 结果可以拿到默认参数 一个空的tuple接收可变参数 一个空的dict接收关键字参数
f1('bbc','ccd')
#传入必选参数 传入默认参数 结果可以拿到传入的默认参数 一个空的tuple接收可变参数 一个空的dict接收关键字参数
f1('bbc','ccd','gfdg')
#传入必选参数 默认参数 可变参数 关键字参数 看打印结果 可变参数虽然用一个tuple来接收 但是传的时候还是要一个一个传
#以下两种打印结果一样
#**{'ff':'vv','bb':"nnn"} ff='vv',bb='nnn'两者传参方式一样
f1('dsgsdf','fsdf','fdsfs',12,323,23,**{'ff':'vv','bb':"nnn"})
f1('dsgsdf','fsdf','fdsfs',12,323,23,ff='vv',bb='nnn')
#如果可变参数真的想传入一个tuple 在传参的时候前边加*
f1('dsgsdf','fsdf','fdsfs',*(12,323,23),**{'ff':'vv','bb':"nnn"})
f1('dsgsdf','fsdf','fdsfs',*(12,323,23),ff='vv',bb='nnn')
f2('bbc','ccd')
#传入必选参数 传入默认参数 结果可以拿到传入的默认参数 一个空的tuple接收可变参数 一个空的dict接收关键字参数
f2('bbc','ccd','gfdg')
#命名关键字参数可以有缺省值
#以下两种打印结果一样
#**{'ff':'vv','bb':"nnn"} ff='vv',bb='nnn'两者传参方式一样
f2('dsgsdf','fsdf','fdsfs',d='我是关键字参数',**{'ff':'vv','bb':"nnn"})
f2('dsgsdf','fsdf','fdsfs',d='我是关键字参数',ff='vv',bb='nnn')
#递归函数调用
print(fact(10))
