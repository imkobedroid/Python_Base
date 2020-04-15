# 生成器

#
# G = [x * x for x in range(10)]
# print(G)
#
# L = (x * x for x in range(10))
# print(L)
# print(next(L))
# print(next(L))
# print(next(L))
# print(next(L))
# print(next(L))
#
# for n in L:
#     print(n)


# def average():
#     total = 0.0  # 数字的总和
#     count = 0  # 数字的个数
#     avg = None  # 平均值
#     while True:
#         num = yield avg
#         print('传入的值是:', num)
#         total += num
#         count += 1
#         print('分母是:', count)
#         avg = total / count
#         print('计算结果是:', avg)
#
#
# def wrap_average(generator):
#     yield from generator
#
#
# # 定义一个函数，通过这个函数向average函数发送数值
# def main(wrap):
#     print(next(wrap))  # 启动生成器
#     print(wrap.send(10))  # 10
#     print(wrap.send(20))  # 15
#     print(wrap.send(30))  # 20
#     print(wrap.send(40))  # 25
#
#
# g = average()
# wrap = wrap_average(g)
# main(wrap)


# 生成器yield与yield from区别简单理解

# yield不仅可以返回值，也可以接收值


# yield返回值, 生成器
# def gen():
#     for x in range(10):
#         yield x
#
#
# print(list(gen()))
#
# for x in gen():
#     print(x)


# yield接收值, 协程

# def gen():
#     while True:
#         x = yield
#         print('我接受到的值是:%s' % x)
#
#
# a = gen()
# next(a)
# a.send(10)
# a.send(20)
# a.send(30)
# a.send(40)


# yield from调用迭代器

# def gen():
#     yield from [1, 2, 3]
#
#
# for i in gen():
#     print(i)
#

# yield from调用生成器
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator

# def sun():
#     while True:
#         x = yield
#         print('我接受到的值是:%s' % x)
#
#
# def gen():
#     yield from sun()
#
#
# def main(wrap):
#     next(wrap)
#     wrap.send(11)
#     wrap.send(22)
#     wrap.send(33)
#
#
# main(gen())


# 调用方 .send(None) 后，在 子生成器 break 时抛出 StopIteration 异常，return 返回值后在委托生成器中赋值给 yield from 表达式左侧变量并捕捉 子生成器 抛出的 StopIteration 异常。
# 问题：
# 但是为什么此时如果 委托生成器 没有 while True: ，又会抛出 StopIteration 异常？


# def gen():
#     """子生成器"""
#     yield 1
#
#
# def gen1(gen):
#     """委托生成器"""
#     yield from gen
#
#
# def main():
#     """调用方"""
#     g = gen()
#     g1 = gen1(g)
#     next(g1)  # 预刺激生成器
#     g1.send(None)  # 启动生成器


# -------------------------------------------------------------------------------------


final_result = {}


# 子生成器
def salesNum(key):
    total = 0
    nums = []

    while True:  # 使用while循环不断的从调用方接收值
        x = yield
        print(key, "- 销量统计:%s" % x)
        if not x:
            break
        total += x
        nums.append(x)
    return total, nums


# 委托生成器

def sales(key):
    while True:
        final_result[key] = yield from salesNum(key)
        print(key + '销量统计完成')


def perform():
    data_set = {
        '牙膏': [100, 200, 300],
        '衣服': [400, 500, 600],
        '鞋子': [700, 800, 900]
    }
    for key, data in data_set.items():
        print('start key:', key)
        s = sales(key)
        next(s)
        for i in data:
            s.send(i)
        s.send(None)
    print('final_result:', final_result)


perform()
