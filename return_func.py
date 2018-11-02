#以函数作为函数的返回值
#高阶函数除了可以接收函数作为参数之外，还可以接收函数作为返回值
#这是一个普通的求和函数
def calc_sum(*args):
    ax = 0;
    for n in args:
        ax+=n
    return ax
print(calc_sum(*list(range(101))))
#函数本身返回一个函数
def lazy_sum(*args):
    def calc_su():
        ax = 0;
        for n in args:
            ax+=n
        return ax
    return calc_su
f = lazy_sum(*list(range(11)))
print(f)
print(f())
#lazy_sum中又定义了函数calc_su ，并且，内部函数 sum
# 可以引用外部函数lazy_sum 的参数和局部变量，当lazy_sum返
#回函数sum 时，相关参数和变量都保存在返回的函数中，这种称为
# “闭包(Closure)”的程序结构拥有极大的威力。

