#!/usr/bin/env python3
# -*- coding: utf-8 -*-
gt = 'ggl'
gt2 = 'ggk'
gt3 = 'ggl'
#比较两个字符串是否是一样 就像java的equals一样
print(gt.__eq__(gt2),gt.__eq__(gt3))
print('please input you age:')
age = input()
#因为用户输入的字符串是str
age = int(age)
if age>=18:
    print('you age is %s,you are adult'%(age))
elif age>=6:
    print('you age is %s,you are tennager'%(age))
else:
    print('too young too simple,simetimes naive')

