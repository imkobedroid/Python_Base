classmates = ["张三", "李四", "bob"]
print(classmates)
print(classmates[0])
print(len(classmates))
# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
print(classmates[-1])
print(classmates[-2])

classmates.append("kobe")
print(classmates)
classmates.insert(0, "dong")
print(classmates)
# 要删除list末尾的元素，用pop()方法：
classmates.pop()
print(classmates)
classmates.pop(0)
print(classmates)

# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
classmates[0] = "李四"
print(classmates)

# list里面的元素的数据类型也可以不同，比如：
L = ['Apple', 123, True]
print(L)

# list元素也可以是另一个list，比如：
List = ["1", "2", [3, 4], "5"]
print(List)
print(List[2])
print(len(List))

# tuple  小括号
# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：

classmates = ('Michael', 'Bob', 'Tracy')
# 要定义一个只有1个元素的tuple，如果你这么定义
T = (1,)
L = ("a", "b", ["c", "d"], "e")
print(L[2][0])
print(L[2][1])
L[2][1] = "f"
print(L[2][1])
