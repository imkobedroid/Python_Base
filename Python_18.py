class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Student name is %s" % self.name

    _repr_ = __str__


print(Student("kobe"))
Student("kobe")


# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__(
# )方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。 我们以斐波那契数列为例，写一个Fib类，可以作用于for循环：

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值


f = Fib()
for n in f:
    print(n)


# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：


class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


f = Fib()
print(f[0])
print(f[1])
print(f[2])
print(f[3])


# 对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：


class Fib_1(object):
    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        elif isinstance(item, slice):
            start = item.start
            stop = item.stop

            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


f1 = Fib_1()
print(f1[0:5])
print(f1[:10])


class Student(object):
    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        if item == "score":
            return 100


class Student(object):
    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        if item == "score":
            return lambda: 25


print(Student("kobe").score)


class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print('My name is %s.' % self.name)


print(Student("kobe")())

# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
print(callable(Student("kobe")))
print(callable('str'))
print(callable([1, 2, 3]))
