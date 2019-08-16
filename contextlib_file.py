# 并不是只有open()函数返回的fp对象才能使用with语句。实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。
# 实现上下文管理是通过__enter__和__exit__这两个方法实现的。例如，下面的class实现了这两个方法：
from contextlib import contextmanager


class Query2(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)


# @contextmanager这个decorator接受一个generator，
# 用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了：
@contextmanager
def create_query(name):
    print('Begin')
    dd = Query2(name)
    yield dd
    print('End')


class Query(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)


with Query('臭傻逼') as q:
    q.query()

with create_query('臭傻逼') as qq:
    qq.query()


# 很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)


with tag('h1'):
    print('Hello')
    print('World')
