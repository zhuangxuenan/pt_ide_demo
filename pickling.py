# 把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，
# 在其他语言中也被称之为serialization，marshalling，flattening等等
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
# Python提供了pickle模块来实现序列化。
import pickle
import json


class Time(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


d = dict(name='Bob', age=20, score=88)
with open('D:\py_img\pickle.txt', 'wb') as f:
    # 序列化
    # 把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件
    pickle.dump(d, f)
with open('D:\py_img\pickle.txt', 'rb') as f2:
    # 反序列化
    # 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象
    d2 = pickle.load(f2)
    print(d2)
# json的序列化与反序列化
json_s = json.dumps(dict(name='Bob', age=20, score=88))
print(json_s)
print(json.loads(json_s))
# 将一个类的实例转换为json 序列化
t = Time('二狗子', 13, 89)
tg = json.dumps(t, default=lambda obj: obj.__dict__, ensure_ascii=False)  # 设置ensure_ascii可以防止中文乱码
print(tg)
# 将一个json转成一个对象 反序列化
fff = json.loads(tg)  # 一个dict
t2 = Time(fff['name'], fff['age'], fff['score'])
print(t2)
