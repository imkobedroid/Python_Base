print(2 > 3)
# 把True变成False，False变成True：
print(not 2 > 3)

a = True
b = False
# 只有所有都为True，and运算结果才是True：
print(a and b)
# 只要其中有一个为True，or运算结果就是True：
print(a or b)

# 同一个变量可以反复赋值，而且可以是不同类型的变量
a = 100
print(a)
a = "kobe"
print(a)

x = 10
x = x + 2
print(x)

a = "ABC"
b = a
print(b)

# 字符串的ASCII转换
print(ord("A"))
print(chr(65))
