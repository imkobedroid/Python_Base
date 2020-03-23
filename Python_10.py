def calc_sum(*a):
    index = 0
    for x in a:
        index = x + index

    return index


print(calc_sum(1, 2, 3, 4, 5))


def calc_sum(a):
    index = 0
    for x in a:
        index = x + index

    return index


print(calc_sum([1, 2, 3, 4, 5]))


# 返回一个函数
def lazy_sum(*args):
    def sumFun():
        index = 0
        for x in args:
            index = index + x
        return index

    return sumFun


print(lazy_sum(1, 2, 3))
print(lazy_sum(1, 2, 3)())

# 在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力
# 请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：

print(lazy_sum(1, 2, 3) == lazy_sum(1, 2, 3))


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


# 每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了。
f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


# 全部都是9,原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

def count():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())
