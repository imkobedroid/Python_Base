import functools
import time

print(list(map(lambda x: x * x, [1, 2, 3, 4, 5])))

f = lambda x: x + 1
print(f(1))


def fun():
    return lambda x: x + 1


print(fun()(1))


def is_odd():
    return lambda n: n % 2 == 1


print(is_odd()(2))


# 函数负值给变量


def A():
    return print("kobe")


a = A

print(a())

# 拿到函数的名字

print(A.__name__)
print(A.__class__)

print("----------------------------")


def log(func):
    def wrapper(x, y):
        print('call %s():' % func.__name__)
        return func(x, y)

    return wrapper


@log
def now(x, y):
    print("你好")
    print("计算结果是:" + str(x + y))


now(1, 2)

log(now)(1, 2)


def fn(*a, **b):
    for x in a:
        print(x)
    for y in b:
        print(y)


# log(fn)(1, 2, 3)

print("++++++++++++++++++++++++++++++++++++++++++")


def log(text):
    def decorator(func):
        print("第一层函数")

        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('execute')
def now():
    print('2015-3-25')


now()

name = log('execute')(now).__name__
print(name)


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


name = log("你好")(now).__name__
print(name)


# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
def metric(fn):
    print('%s executed in %s ms' % (fn.__name__, 10.24))
    return fn


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


def timeTest(fun):
    print('%s executed in %s ms' % (fun.__name__, 100))
    return fun


@timeTest
def A():
    print("我是函数A")


@timeTest
def B():
    print("我是函数B")


def C():
    print("我是函数C")


print(timeTest(C)())
print(B())
print(A())
