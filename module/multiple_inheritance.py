# 本示例主要用来讲解多重继承
class Animal2(object):
    def cry(self):
        print("我是一个会叫的小动物")


# 哺乳类
class Mammal(Animal2):
    def temperature(self):
        print('我是一只恒温哺乳动物')


# 鸟类
class Bird(Animal2):
    def temperature(self):
        print('我是一只恒温鸟类')


# 可以跑的动物
class Runnable(object):
    def run(self):
        print('瞎几把跑吧...')


# 可以飞的动物
class Flyable(object):
    def fly(self):
        print('我要飞得更高...')


# 各种动物:
class Dog2(Mammal, Runnable):
    pass


class Cat2(Mammal):
    pass


# 各种鸟
class Parrot(Bird,Flyable):
    pass


class Ostrich(Bird):
    pass
