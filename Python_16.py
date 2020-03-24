# 获取对象信息

# 使用type()


print(type(123))

abs = 123
print(type(abs))


# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：


def fun():
    pass


print(type(fun))
print(type(lambda x: x + 1))
print(type(x for x in range(10)))


class Animal(object):
    pass


class Dog(Animal):
    pass


class Cat(Animal):
    pass


dog = Dog()
cat = Cat()
animal = Animal()

print(isinstance(dog, Animal))
print(isinstance(cat, Animal))
print(isinstance(cat, Cat))
print(isinstance(animal, Cat))
print(isinstance(animal, Dog))
print(isinstance('a', str))
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print(dir('ABC'))

len('ABC')
# 等价于
'ABC'.__len__()


class MyDog(object):
    def __len__(self):
        return 100


print(MyDog().__len__())

print('ABC'.lower())


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()
print(hasattr(obj, 'x'))
print(obj.x)


# >>> hasattr(obj, 'x') # 有属性'x'吗？
# True
# >>> obj.x
# 9
# >>> hasattr(obj, 'y') # 有属性'y'吗？
# False
# >>> setattr(obj, 'y', 19) # 设置一个属性'y'
# >>> hasattr(obj, 'y') # 有属性'y'吗？
# True
# >>> getattr(obj, 'y') # 获取属性'y'
# 19
# >>> obj.y # 获取属性'y'
# 19
# >>> getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404


# >>> hasattr(obj, 'power') # 有属性'power'吗？
# True
# >>> getattr(obj, 'power') # 获取属性'power'
# <bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
# >>> fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
# >>> fn # fn指向obj.power
# <bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
# >>> fn() # 调用fn()与调用obj.power()是一样的
# 81


class Student(object):
    def __init__(self, name):
        self.name = name


s = Student("kobe")

print(s.name)


class Student(object):
    name = 'Student'


s = Student()
print(Student().name)
print(Student.name)

s.name = "dong"

print(s.name)
print(Student.name)

del s.name
# 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
print(s.name)
