#Date 2018.10.22
#函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言
#编写的函数没有变量，因此，任意一个函数，只要输入是确定的，输出
#就是确定的，这种纯函数我们称之为没有副作用。而允许使用变量的程
#序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到
#不同的输出，因此，这种函数是有副作用的。
#函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函
#数，还允许返回一个函数！
#Python 对函数式编程提供部分支持。由于 Python 允许使用变量，因此，
#Python 不是纯函数式编程语言

#高阶函数 Higher-order function

#函数本身也可以赋值给变量，即：变量可以指向函数


x = abs(-100)#函数赋值给变量
y = abs#函数本身赋值给变量
print(x,y)#打印结果 10 <built-in function abs>
#如果一个变量指向了一个函数，那么，可否通过该变量来调用这个函数
print(y(-10))#打印结果：10
#说明变量 y 现在已经指向了 abs 函数本身。直接调用 abs() 函数和调用变量 y() 完全相同
#函数名也是变量
#那么函数名是什么呢？
#函数名其实就是指向函数的变量！对于 abs() 这个函数，
#完全可以把函数名 abs 看成变量，它指向一个可以计算绝对值的函数！

#传入函数
#既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以
#接收另一个函数作为参数，这种函数就称之为高阶函数
#比如
def add(a,b,y):
    return y(a)+y(b)
print(add(-1,-1,abs))#abs作为一个一个参数传入
#编写高阶函数，就是让函数的参数能够接收别的函数。

#python内置函数 map() reduce()
#map() 函数接收两个参数，一个是函数，一个是 Iterable ，map 将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator 返回
#比如我们有一个函数 f(x)=x^2 ，要把这个函数作用在一个 list
# [1,2, 3, 4, 5, 6, 7, 8, 9] 上，就可以用 map()
def f(x):
    return x*x
y= map(f,[1,2, 3, 4, 5, 6, 7, 8, 9])
print(y)
print(list(y))
#map() 传入的第一个参数是f，即函数对象本身。由于结果y是一个
#Iterator,Iterator是惰性序列，因此通过list()函数让它把整个序列都
#计算出来并返回一个 list
#再比如把一个list都转成字符串
print(list(map(str,[1,2,3,4,5,6,7,8,9])))
#map() 作为高阶函数，事实上它把运算规则抽象了

#reduce
#reduce 把一个函数作用在一个序列 [x1, x2, x3, ...]
#上，这个函数必须接收两个参数， reduce 把结果继续和序列的下一个元
#素做累积计算，其效果就是：
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
#可以用于队列求和
from functools import reduce
def add(x,y):
    return x+y
def fn(x,y):
    return x*10+y
def normalize(name):
    return name.capitalize()
def pord(x,y):
    return x*y
print(reduce(add,[1,2,3,4,5,6,7,8,9]))#list
print(reduce(add,(1,2,3,4,5,6,7,8,9)))#tuple
print(reduce(fn,[1,3,5,7,9]))
L1 = ['AdmIn','anny','LUCY','sandY','wILl']
print(list(map(normalize,L1)))
print('3*5*7*9=',reduce(pord,[3,5,7,9]))
#filter
#用于过滤序列 接收一个函数一个序列
def is_odd(n):
    return n%2==1
print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9])))#返回一个奇数序列
def is_empty(s):
    return s and s.strip()
s_s = ['A', '', 'B', None, 'C', ' ']
print(list(filter(is_empty,s_s)))
# filter() 函数返回的是一个Iterator也就是一个惰性序列，所
#以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list

#2018.11.06 匿名函数
#关键字 lambda 表示匿名函数，冒号前面的 x 表示函数参数。
#匿名函数有个限制，就是只能有一个表达式，不用写 return ，返回值就是该表达式的结果。
#用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，
#匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
print("---------lambda-----------")
print(list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9])))
fg = lambda x:x*x*2
print(fg)
print(fg(55))
#可以把匿名函数作为返回值返回
def build(x,y):
    return lambda: x*x+y*y
#看打印结果
gg = build(11,22)
print(gg)
print(gg())
#lambda只是一个表达式，函数体比 def 简单很多。
#lambda的主体是一个表达式，而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去。
#lambda函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
#虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
#-----------------------------以下↓存疑---------------------------------------------
#这个鬼有点不明白 感觉没啥子卵用 先记下
#Decorator装饰器
#在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
#装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，
# 装饰器的返回值也是一个函数对象。它经常用于有切面需求的场景，
# 比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。装饰器是解决这类问题的绝佳设计，
# 有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用。
#概括的讲，装饰器的作用就是为已经存在的函数或对象添加额外的功能。
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper
@log
def now():
    print("今天是个好日子")
print(now())
print(now.__name__)#此处返回的是now
#-----------------------------以上存疑↑---------------------------------------------
print('----------装饰器-------------------')
#偏函数
#int(s,base)  将其他进制转换为十进制 s为要转化为数值类型的字符串，base则为转换前的进制。
print(int("1234"))#默认十进制
print(int("1234",base=8))#将8进制转换成10进制
print(int("1234",base=16))#将16进制转换成10进制
def int2(x,base=2):
    return int(x,base)
print("默认将2进制转换10进制:",int2("1000000"))
print("默认将10字符串转成10进制整数:",int2("12345",10))
print("默认将8进制转换成10进制:",int2("777777",8))
print("默认将16进制转成成10进制:",int2("FFFF",16))
#functools.partial 的作用就是，把一个函数的某些参数给固定住
#（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
int2 = functools.partial(int,base=2)
print(int2('100000'))
