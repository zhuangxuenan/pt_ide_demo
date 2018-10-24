#排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，
#排序的核心是比较两个元素的大小。如果是数字，我们可以直接比较，
#但如果是字符串或者两个 dict 呢？直接比较数学上的大小是没有意义
#的，因此，比较的过程必须通过函数抽象出来。通常规定，对于两个元
#素 x 和 y ，如果认为 x < y ，则返回 -1 ，如果认为 x == y ，则返回 0 ，如
#果认为 x > y ，则返回 1 ，这样，排序算法就不用关心具体的比较过程，
#而是根据比较结果直接排序。
#Python 内置的 sorted() 函数就可以对 list 进行排序
l1 = sorted([36, 5, -12, 9, -21])
l2 = sorted([36, 5, -12, 9, -21], key=abs)#接收一个 key 函数来实现自定义的排序
l3 = sorted(['bob', 'about', 'Zoo', 'Credit'])
#key 指定的函数将作用于 list 的每一个元素上，并根据 key 函数返回的结果进行排序
l4 = sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower)
#要进行反向排序，不必改动key函数，可以传入第三个参数 reverse=True
l5 = sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True)
l6 = sorted([36, 5, -12, 9, -21], key=abs,reverse=True)
print(l1)
print(l2)
print(l3)
print(l4)
print(l5)
print(l6)
#sorted() 也是一个高阶函数。用 sorted() 排序的关键在于实现一个映射函数