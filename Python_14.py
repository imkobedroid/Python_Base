# 访问限制


class Student(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def getName(self):
        return self._name

    def getAge(self):
        return self._age

    def print_age(self):
        print("%s 的年龄是: %s" % (self._name, self._age))


instance = Student("kobe", 40)

print(instance.name)
print(instance.age)
print(instance.getName())
print(instance.getAge())
print(instance.print_age())

# 表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。不信试试：
instance._age = 60
print(instance._age)
print(instance.getAge())
print(instance.age())
