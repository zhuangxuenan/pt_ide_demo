#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from module.test_class import Student, Dog, Cat, People, Animal, Teacher, Tables, Fib,MyList
from module.multiple_inheritance import Dog2, Cat2, Parrot, Ostrich
import types

student = Student('王八羔子', 80)
student.print_score()
# 如果给外部变量添加 下划线“_”就可以让该变量变成一个私有变量而且从外部无法访问
student.name = '张三'
student.print_score()
print("这个家伙的成绩标准是：" + student.get_grade())
student.set_score(50)
student.print_score()
print("这个家伙的成绩标准是：" + student.get_grade())
dog = Dog()
dog.run()
cat = Cat()
cat.run()
people = People()


# 对于静态语言（例如Java）来说，如果需要传入Animal类型，
# 则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。
# 我们只需要保证传入的对象有一个run()方法就可以了：
# 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子
# Python的“file-like object“就是一种鸭子类型。对真正的文件对象，
# 它有一个read()方法，返回其内容。但是，许多对象，只要有read()方法，
# 都被视为“file-like object“。许多函数接收的参数就是“file-like object“，
# 你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。
def run_twice(an):
    if hasattr(an, 'run'):
        an.run()
    return None


print('鸭子类型打印分割线----------------------')
run_twice(dog)
run_twice(cat)
run_twice(people)
print('type()分割线------------------------------')
# type()函数：判断对象类型
# 基本类型 函数 类都可以使用：
print(type(123))
print(type('编的跟真的一样'))
print(type(True))
print(type(dog))
print(type(cat))
print(type(abs))
# 判断对象是否是函数 使用types模块中定义的常量 import types
print(type(run_twice) == types.FunctionType)
print(type(abs) == types.FunctionType)
print('isinstance()分割线------------------------------')
# 判断class的类型，使用isinstance()函数
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(isinstance(cat, Cat))
print(isinstance(cat, Animal))
print(isinstance(dog, Cat))
# 判断一个变量是否是某些类型中的一种
print(isinstance((1, 2, 3), (list, tuple)))
print(isinstance([1, 2, 3], (list, tuple)))
# 获得一个对象的所有属性和方法，使用dir()函数
print(dir(dog))
print(dir('str'))
if not hasattr(student, 'sex'):
    student.sex = '男'
print(student.sex)
teacher = Teacher("二狗子", 30)
teacher.print_other()
# teacher.sex = '男' 错误 在类中通过__slots__已经限制了只能添加name age两个属性

tables = Tables()
tables.score = 80
print('成绩是：' + str(tables.score) + '----所在级别：' + tables.grade)
print('多重继承分割线-------------------')
dog2 = Dog2()
cat2 = Cat2()
parrot = Parrot()
ostrich = Ostrich()
dog2.cry()
dog2.temperature()
dog2.run()
print('----------------------------------')
cat2.cry()
cat2.temperature()
print('----------------------------------')
parrot.cry()
parrot.temperature()
parrot.fly()
print('----------------------------------')
ostrich.cry()
ostrich.temperature()
# 定制类
# 一个类作用于for循环
for n in Fib():
    print(n)
# 根据下标取出元素
f = Fib()
print(f[0], f[1], f[2], f[3], f[4], f[5], f[6], f[7], f[8], f[9])
print(f[:10])  # 传入的不是整数 是个切片


# 枚举类

# type()
# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
# 在静态语言中 不论是函数 类还是变量 必须先定义后使用
# 但是在python中 type()函数既可以返回一个对象的类型，又可以创建出新的类型，
# 比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：
def fn(self, name='world'):  # 先定义函数
    print('Hello %s' % name)
# 要创建一个class对象，type()函数依次传入3个参数：
    # class的名称；
    # 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；(第二个参数是个父类的tuple集合，一个元素的tuple要在括号中加,)
    # class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
Hello = type('Hello', (object,), dict(hello=fn))  # 创建hello class
h = Hello()
h.hello()
print(type(Hello))
print(type(h))
# 使用metaclass来创建类
L = MyList()
L.add(1)
print(L)
