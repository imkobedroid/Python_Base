import asyncio
import threading


# @asyncio.coroutine
# def hello():
#     print('hello world')
#     yield from asyncio.sleep(1)
#     print('hello again')
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()

#
# @asyncio.coroutine
# def hello():
#     print('Hello world! (%s)' % threading.currentThread())
#     yield from asyncio.sleep(1)
#     print('Hello again! (%s)' % threading.currentThread())
#
#
# task = [hello(), hello()]
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(task))
# loop.close()


# 请注意，async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：
#
# 把@asyncio.coroutine替换为async；
# 把yield from替换为await。


async def hello():
    print('hello world (%s)' % threading.currentThread())
    await asyncio.sleep(1)
    print('hello again (%s)' % threading.currentThread())


loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()

# 因为yield关键字标记了一个函数为generator，所以又一个next方法进行迭代，碰到yield后就不执行了并返回这个yield后面的值
# def hello():
#     print('hello world')
#     yield '我暂停,并返回了'
#     print('我继续执行了')
#     yield '我又暂停了，并返回了'
#
#
# h = hello()
# print(next(h))
# print(next(h))


# def generator_1(title1):
#     yield title1
#
#
# def generator_2(title):
#     yield from title
#
#
# titles = ['python', 'java', 'c++']
#
# for title in generator_1(titles):
#     print('生成器1:', title)
#
# for title in generator_2(titles):
#     print('生成器2:', title)


# def hello():
#     print('hello world')
#     yield from '我暂停,并返回了'
#     print('我继续执行了')
#     yield from '我又暂停了，并返回了'
#
#
# h = hello()
# print(next(h))
# print(next(h))
# print(next(h))
