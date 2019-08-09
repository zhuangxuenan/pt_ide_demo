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
