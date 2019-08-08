#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
' python文档注释 a test module '
__author__ = '阳光下的影子'
def test():
    args = sys.argv
    print(args)
    if len(args)==1:
        print('Hello>>>>>>>>World')
    elif len(args)==2:
        print('Hello %s'%args[1])
    else:
        print('too many arguments')

test()
if __name__=='__main__':
    test()