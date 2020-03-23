from pip._vendor.distlib.compat import raw_input

a = 20
if a > 10:
    print('我的年龄是', a)
else:
    print('我的年龄是', 10)

b = 20
if b > 10:
    print("我的年龄大于", 10)
elif b < 30:
    print("我的年龄小于", 30)
else:
    print("我的年龄未知")

names = ["kobe", "dong", "mac"]
for name in names:
    print(name)

Sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    Sum += x
print(Sum)

print(range(5))

Sum = 0
for x in range(10):
    Sum += x
print(Sum)

Sum = 0
n = 99
while n > 0:
    Sum += n
    n -= 2
print(Sum)

birth = int(input('birth: '))
if birth > 2000:
    print('00后')
else:
    print('90后')
