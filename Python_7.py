# 递归函数
from collections import Iterable


def fact(x):
    if x == 1:
        return x
    return x * fact(x - 1)


print(fact(1))
print(fact(4))

# 切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])
print(L[0:4])
# 第一个是0还可以省略
print(L[:3])

print(L[-1:])
print(L[-2:])

L = list(range(100))
print(L)
print(L[10:20])
print(L[-10:])
# 前10个数，每两个取一个
print(L[:10:2])
# 所有数，每5个取一个
print(L[::5])
# 元组也可以
print((0, 1, 2, 3, 4, 5)[:3])

# 迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d.keys():
    print(key)

for value in d.values():
    print(value)

for key, value in d.items():
    print(key, value)

for v in 'ABC':
    print(v)

# 如何判断一个对象是可迭代对象呢

print(isinstance('adc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance((1, 2, 3), Iterable))
print(isinstance({"key1": 1, "key2": 2}, Iterable))
print(isinstance(123, Iterable))

# 下标
for i, value in enumerate([1, 2, 3, 4, 5, 6]):
    print(1, value)

for x, y in [(1, 1), (2, 4), (3, 8)]:
    print(x, y)

# 生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？
L = [x * x for x in range(1, 11)]
print(L)

L = [x * x for x in range(1, 11) if x % 2 == 0]
print(L)

L = [m + n for m in 'ABC' for n in 'DEF']
print(L)

d = {'x': 'A', 'y': 'B', 'z': 'C'}
L = [k + "=" + v for k, v in d.items()]
print(L)

L = ['Hello', 'World', 'IBM', 'Apple']
S = [s.lower() for s in L]
print(S)

# 在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else。
