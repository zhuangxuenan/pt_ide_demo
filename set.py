#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#set和dict类似也是一组key的集合但不存储 value由于key不能重复,所以，在 set中没有重复的 key
#set并不是有序的 有键无值的dict
p = set([1,3,'dsfsd',5,'fsdfdsf'])
print(p)
p2 = {1,3,5,7,9,11,13,15,17}
print(p2)
#因为set中没有重复的元素 所以他可以自动去重
p3 = {1,2,3,3,4,5,6,6,7,7,8}
print(p3)
#通过 add(key) 方法可以添加元素到 set 中，可以重复添加，但不会有效果：
p2.add(65)
print(p2)
#集合取交集
print(p2&p3)
#集合取并集
print(p2|p3)
