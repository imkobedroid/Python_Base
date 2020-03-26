# 断言
import logging

logging.basicConfig(level=logging.INFO)


def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n


print(foo(2))
# print(foo(0))

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

s = '0'
n = int(s)
print(10 / n)
