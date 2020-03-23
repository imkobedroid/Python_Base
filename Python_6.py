import math

print(abs(-100))
print(max(1, 2, 3, 4))
print(int(123))

# 函数 变量
a = abs
print(a(-19))


# 定义函数
def my_abs(x: int):
    if x > 100:
        print(x)
    else:
        print(x + 100)
        return x + 200


print(my_abs(99))


# 如果想定义一个什么事也不做的空函数，可以用pass语句：
# pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
def pop():
    pass


age = 100
if age >= 100:
    pass


# 让我们修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现：
def my_abs(x: (int, float)):
    if x > 100:
        print(x)
    else:
        print(x + 100)


print(my_abs(100))
print(my_abs(100.1))


# 返回多个值

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


print(move(1, 2, 4))
print(move(1, 2, 4)[0])
print(move(1, 2, 4)[1])

x, y = move(1, 2, 4)
print(x)
print(y)


def power(f, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * f
    return s


print(power(5, 2))
print(power(3, 2))
print(power(3))


# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
def add_end(name=['end']):
    if name is None:
        name = []
    name.append("end")
    return name


print(add_end(["1", "2", "3"]))
print(add_end())
print(add_end())
print(add_end())


def test1(a=[]):
    a.append("1")
    return a


print(test1())
print(test1())


# 定义默认参数要牢记一点：默认参数必须指向不变对象，例如常量，元组！如果参数可变例如集合[]，就会出现上面指向对象的情况，而不管对象里面的内容，
def test(x=1):
    x += 1
    return x


print(test())
print(test())


def test1(a=(5)):
    return a


print(test1())
print(test1())


def add_end(s=None):
    if s is None:
        s = []
    s.append("end")
    return s


print(add_end(["1"]))
print(add_end(["1"]))
print(add_end())
print(add_end())


# 可变参数

def calc(*num):
    s = 0
    for item in num:
        s += item * item
    return s


print(calc(1, 2, 3))
print(calc(1, 2))

# 把list或tuple的元素变成可变参数传进去：

A = [1, 2, 3]
B = (1, 2)
print(calc(*A))
print(calc(*B))


# 关键字参数

def person(name, age, **other):
    print("name:", name, "age:", age, "other:", other)
    return other


def person1(name, age, **other):
    return other


# 想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。
person("kobe", 40)
person("kobe", 40, 职业="篮球", 喜欢="足球")

print(person1("kobe", 40, 职业="篮球", 喜欢="足球").keys())
print(person1("kobe", 40, 职业="篮球", 喜欢="足球").values())
print(person1("kobe", 40, 职业="篮球", 喜欢="足球").get("职业"))

extra = {'city': 'Beijing', 'job': 'Engineer'}
person("kobe", "40", city=extra['city'], job=extra['job'])
person("kobe", "40", **extra)


# 命名关键字参数

def person(name, age, **other):
    if '职业' in other:
        pass
    if '喜欢' in other:
        pass
    print('name:', name, 'age:', age, 'other:', other)


person("小明", 26, 职业='程序员', 喜欢='篮球')
person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)


# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person(name, age, *, city, job):
    print("name:", name, "age:", age, "other:", city, job)


person("kobe", 40, city="美国", job="篮球运动员")


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name, age, *args, city, job):
    print(name, age, args, city, job)


person("kobe", 40, "身高193", "喜欢牛排", job="职业篮球运动员", city="美国")


def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)


person("kobe", 40, job="职业篮球运动员")


# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
