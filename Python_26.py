# 常用的内建模块


# 获取当前datetime
import argparse
import itertools
import os
from collections import namedtuple, deque, defaultdict, ChainMap, Counter
from contextlib import contextmanager, closing
from datetime import datetime
from urllib.request import urlopen

print(datetime.now())

dt = datetime(2015, 4, 19, 12, 20)  # 用指定日期时间创建datetime
print(dt)
print(dt.timestamp())

s = 1429417200.0
print(datetime.fromtimestamp(s))

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

print(datetime.now().strftime('%a, %b %d %H:%M'))

point = namedtuple('point', ['x', 'y'])
p = point(1, 2)
print(p.x)
print(p.y)

print(isinstance(p, point))
print(isinstance(p, tuple))

# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = "abc"
print(dd['key1'])
print(dd['key2'])
print(dd['key3'])

defaults = {
    'color': 'red',
    'user': 'guest'
}
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v}
combined = ChainMap(command_line_args, os.environ, defaults)
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])

# Counter是一个简单的计数器，例如，统计字符出现的个数：
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print(c)
c.update('hello')  # 也可以一次性update
print(c)

# itertools
# natuals = itertools.count(1)
# for n in natuals:
#     print(n)

# cs = itertools.cycle('ABC')
# for c in cs:
#     print(c)

ns = itertools.repeat('A', 3)  # 不过如果提供第二个参数就可以限定重复次数：
for a in ns:
    print(a)

na = itertools.count(1)
ns = itertools.takewhile(lambda x: x < 10, na)
print(list(ns))
print(ns)

for c in itertools.chain('abc', 'def'):
    print(c)

# groupby()把迭代器中相邻的重复元素挑出来放在一起：
for key, group in itertools.groupby('AAABBBCCC'):
    print(key, list(group))

# 实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，而函数返回值作为组的key。如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))


# 并不是只有open()函数返回的fp对象才能使用with语句。实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句

class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)


with Query('BOB') as q:
    q.query()


# 编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法，上面的代码可以改写如下：


class QueryCls(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)


@contextmanager
def create_query(name):
    print('Begin')
    q = QueryCls(name)
    yield q
    print('End')


with create_query('Bob') as q:
    q.query()


@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)


with tag("h1"):
    print("hello")
    print("world")

# 如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象。例如，用with语句使用urlopen()：
with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)


# closing也是一个经过@contextmanager装饰的generator，这个generator编写起来其实非常简单：

@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()


# 它的作用就是把任意对象变为上下文对象，并支持with语句。
# @contextlib还有一些其他decorator，便于我们编写更简洁的代码。


print("--------------------------")


# yield 是一个类似 return 的关键字，迭代一次遇到yield时就返回yield后面(右边)的值。重点是：下一次迭代时，从上一次迭代遇到的yield后面的代码(下一行)开始执行。


class QueryCls(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)


@contextmanager
def create_query(name):
    print('Begin')
    q = QueryCls(name)
    yield q
    print('End')


with create_query('Bob') as q:
    print(q)
    q.query()
