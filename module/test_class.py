class Student(object):
    # 在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
    # 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去
    def __init__(self, name, score):
        self.name = name
        # 添加下划线可以让变量私有，禁止从外部访问他
        # 如果还想修改这个变量 可以提供外部方法
        self._score = score

    def print_score(self):
        print('个人信息：%s: %s' % (self.name, self._score))

    def get_grade(self):
        if self._score >= 90:
            return 'A'
        elif self._score >= 60:
            return 'B'
        else:
            return 'C'

    def set_score(self, score_up):
        self._score = score_up


class Animal(object):
    def run(self):
        print('Animal is running...')


# 继承
class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


class People():
    def run(self):
        print('People is running...')


class Teacher(object):
    # Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
    __slots__ = ('name', 'age')

    # __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
    def __init__(self, name, age):
        if isinstance(name, str):
            self.name = name
        if isinstance(age, int):
            self.age = age
        elif isinstance(age, float):
            self.age = int(age)
        elif isinstance(age, str):
            self.age = int(age)
        else:
            self.age = 18

    def print_other(self):
        print('教师个人信息：%s: %s' % (self.name, self.age))


class Tables(object):
    # 把一个getter方法变成属性，只需要加上@property就可以了，
    # 此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    # 只读属性
    @property
    def grade(self):
        if self._score >= 90:
            return 'A'
        elif self._score >= 60:
            return 'B'
        else:
            return 'C'


# 定制类
class Exapple(object):
    def __init__(self, name):
        self.name = name

    # 其实就是重写一些函数的函数体 修改返回值
    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__


# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
# 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法
# 拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
# 以斐波那契数列为例 可以作用于for循环
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器

    def __iter__(self):
        return self  # 示例本身就是迭代对象 故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100:
            raise StopIteration
        return self.a

    # 如果想要实现像list那样按照下标取出元素，需要实现__getitem__()方法：
    # 传入的参数可能是个int 也可能是个slice切片
    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        elif isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


'''
metaclass
 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
 metaclass，直译为元类，简单的解释就是：
 当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
 但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
 连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
 所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
'''


# 定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：
# metaclass是类的模板，所以必须从`type`类型派生：
# 给我们自定义的MyList增加一个add方法：
class ListMetaclass(type):
    # 当前准备创建的类的对象；
    # 类的名字；
    # 类继承的父类集合；
    # 类的方法集合。
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


# 当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，
# 要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。
class MyList(list, metaclass=ListMetaclass):
    pass
