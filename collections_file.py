from collections import namedtuple, deque, defaultdict, OrderedDict, ChainMap, Counter
import os, argparse

# namedtuple是一个函数，它用来创建一个自定义的tuple对象，
# 并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
# 这样一来，我们用namedtuple可以很方便地定义一种数据类型，
# 它具备tuple的不变性，又可以根据属性来引用，使用十分方便。
# namedtuple('名称', [属性list]):
# 比如定义一个坐标
Point = namedtuple('Point', ['x', 'y'])
P = Point(1, 2)
print(P.x, P.y)
# 定义一个圆
Circle = namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(10, 10, 5)
print(c.x, c.y, c.r)

# deque
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，
# 因为list是线性存储，数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。
q = deque(['a', 'b', 'c', 'd'])
print(q)
q.append('e')  # 成功
print(q)
q.appendleft(('q', 'w', 'e'))  # 成功
print(q)
q.appendleft(['r', 't', 'y'])  # 成功
print(q)
'''
q.append('x', 'y')  # 失败
q.append(('s', 'g'))  # 成功
q.append(*('s', 'g'))  # 失败
q.appendleft(*['r', 't', 'y'])  # 失败
q.appendleft('x', 'y')  # 失败
'''
# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
# defaultdict是无需的 如果对它进行迭代 可能每次都会回去不同的结果
dd = defaultdict(lambda: 'N/a')
dd['key1'] = 'default'
print(dd['key1'], '- - -分割线- - -', dd['key2'])

# OrderedDict
# 同上 但是它是有顺序的
test_dict = dict([('a', 1), ('b', 2), ('c', 3)])  # 它是无序的
print(test_dict)
for k, v in test_dict.items():
    print(k, v)

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])  # 它是有序的
print(od)
for k, v in od.items():
    print(k, v)


# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


# ChainMap
# ChainMap可以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，
# 但是查找的时候，会按照顺序在内部的dict依次查找。
# 什么时候使用ChainMap最合适？举个例子：应用程序往往都需要传入参数，参数可以通过命令行传入，
# 可以通过环境变量传入，还可以有默认参数。我们可以用ChainMap实现参数的优先级查找，即先查命令行参数，
# 如果没有传入，再查环境变量，如果没有，就使用默认参数。
# 构造缺省参数:
defaults = {
    'color': 'red',
    'user': 'guest'
}

# 构造命令行参数:
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v}

# 组合成ChainMap:
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数:
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])

# Counter 计数器 Counter实际上也是dict的一个子类
c = Counter()
for ch in 'programming':  # 统计字符在字符串中出现的次数
    c[ch] += 1
print(c)
