#Python 内置了字典：dict 的支持，dict 全称 dictionary，在其他语言中也
#称为 map，使用键-值（key-value）存储，具有极快的查找速度
# dict 的 key 必须是不可变对象。比如整数 字符串
#map的键值可以是不同的类型
d={"one":"第一个","two":"第二个","three":13,"four":True}
print(d)
#判断key值是否存在
if "three" in d:
    print(d["three"])
# 通过 dict 提供的 get 方法，如果 key 不存在，可以返回 None，或者
# 自己指定的 value：
print(d.get("onee"))
print(d.get("one"))
print(d.get("onee",-1))
#1. 查找和插入的速度极快，不会随着 key 的增加而增加；
#2. 需要占用大量的内存，内存浪费多
if "two" in d:
    d["two"]="新来的第二个"
print(d)
d["new"]="新添加的元素"
d["boolean"]=False
print(d)
#删除某个键值
d.pop("boolean")
print(d)
#用整数作为键
d[144]="这是用整数来做键的"
print(d)
d['test'] = {'token': '12345', 'status': 'working'}
print(d)
ff = dict(aa = 12,bb = 13,cc = 'ggg',dd = {'token': '12345', 'status': 'working'})
print(ff)