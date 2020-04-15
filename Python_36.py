# yield


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


# def a():
#     print('aaa')
#     p1 = yield '123'
#     print('bbb')
#     if p1 == 'hello':
#         print('p1是send传过来的')
#     p2 = yield '234'
#     print(p2)
#
#
# r = a()
# next(r)
# r.send('hello')

# 说一下执行的顺序，首先a()是个生成器；第一次执行要么next(r)要么r.send(None)，不能使用r.send('xxxxx')；这会报错的。第一次执行时next(r)时，首先打印出aaa,
# 然后遇到yield即跳出，然后执行r.send('hello')时，p1则被赋值为hello了，然后继续接着上次运行，下一步打印出bbb，然后打印出'p1是send传过来的',当再次遇到第二个yield时跳出，所以结果只打印了三行，后面的p2没有执行。
import asyncio
import time


def generator_1():
    total = 0
    while True:
        # print('第一次运行')
        x = yield
        print('加', x)
        if not x:
            print('我退出了')
            break
        total += x
    return total


# a=generator_1()
# a.send(None)
# a.send(2)


# def generator_2():  # 委托生成器
#     while True:
#         total = yield from generator_1()  # 子生成器
#         print('加和总数是:', total)
#
#
# def main():  # 调用方
#     # g1 = generator_1()
#     # g1.send(None)
#     # g1.send(2)
#     # g1.send(3)
#     # g1.send(None)
#     g2 = generator_2()
#     g2.send(None)
#     g2.send(2)
#     g2.send(3)
#     g2.send(None)
#
#
# main()


@asyncio.coroutine  # 标志协程的装饰器
def taskIO_1():
    print('开始运行IO任务1...')
    yield from asyncio.sleep(2)  # 假设该任务耗时2s
    print('IO任务1已完成，耗时2s')
    return taskIO_1.__name__


@asyncio.coroutine  # 标志协程的装饰器
def taskIO_2():
    print('开始运行IO任务2...')
    yield from asyncio.sleep(3)  # 假设该任务耗时3s
    print('IO任务2已完成，耗时3s')
    return taskIO_2.__name__


@asyncio.coroutine  # 标志协程的装饰器
def main():  # 调用方
    tasks = [taskIO_1(), taskIO_2()]  # 把所有任务添加到task中
    done, pending = yield from asyncio.wait(tasks)  # 子生成器
    for r in done:  # done和pending都是一个任务，所以返回结果需要逐个调用result()
        print('协程无序返回值：' + r.result())


if __name__ == '__main__':
    start = time.time()
    loop = asyncio.get_event_loop()  # 创建一个事件循环对象loop
    try:
        loop.run_until_complete(main())  # 完成事件循环，直到最后一个任务结束
    finally:
        loop.close()  # 结束事件循环
    print('所有IO任务总耗时%.5f秒' % float(time.time() - start))
