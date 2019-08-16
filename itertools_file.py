# itertools提供了非常有用的用于操作迭代对象的函数。
import itertools

# count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列
natuals = itertools.count(1)
for n in natuals:
    if n < 5:
        print(n)
    else:
        break

print('- - - - -分割线- - - - -')

# cycle()会把传入的一个序列无限重复下去：停不下来
cs = itertools.cycle('ABC')
sum_s = 0
for c in cs:
    if sum_s < 5:
        print(c, '- - -', sum_s)
        sum_s += 1
    else:
        break

print('- - - - -分割线- - - - -')

nc = itertools.repeat('A', 5)
for n in nc:
    print('repeat', n)
# 无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，
# 它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。
# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
natuals2 = itertools.count(1)
ns = itertools.takewhile(lambda x: x < 10, natuals2)
for n in ns:
    print(n)

print('- - - - -分割线- - - - -')

# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
for xx in itertools.chain('ABC', 'XYZ'):
    print(xx)

print('- - - - -分割线- - - - -')

# groupby()把迭代器中相邻的重复元素挑出来放在一起：
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))

print('- - - - -分割线- - - - -')

# 实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，
# 这两个元素就被认为是在一组的，而函数返回值作为组的key。如果我们要忽略大小写分组
for key, group in itertools.groupby('AaaBBbcCAAa', lambda x: x.upper()):
    print(key, list(group))
