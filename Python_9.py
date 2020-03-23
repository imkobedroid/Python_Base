# map/reduce
from functools import reduce


def f(s):
    return s + 10


L = [1, 2, 3, 4, 5]
R = map(f, L)

print(list(R))


# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

def add(x, y):
    return x + y


s = [1, 3, 5, 7, 9]

print(reduce(add, s))


# 但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：
def toString(x, y):
    return str(x) + str(y)


s = [1, 3, 5, 7, 9]

print(reduce(toString, s))


def toSting1(x, y):
    return x * 10 + y


def toString2(x):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[x]


print(reduce(toSting1, map(toString2, '13579')))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(a):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    return reduce(fn, map(char2num, a))


print(str2int("13579"))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(str2int("13579"))


def is_odd(s):
    return s % 2 == 0


print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, ])))


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

print(sorted([36, 5, -12, 9, -21]))

print(sorted([36, 5, -12, 9, -21], key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# 对上述列表分别按名字排序：
L2 = sorted(L, key=lambda x: x[0])
print(L2)

# 再按成绩从高到低排序：
L3 = sorted(L, key=lambda x: x[1], reverse=True)
print(L3)
