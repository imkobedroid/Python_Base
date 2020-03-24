# 使用__slots__
from types import MethodType


class Student(object):
    pass


s = Student()

s.name = "kobe"
print(s.name)


# 给类绑定方法
def set_age(self, age):
    self.age = age


s.set_age = MethodType(set_age, s)
s.set_age(40)
print(s.age)


# 但是，给一个实例绑定的方法，对另一个实例是不起作用的

# 为了给所有实例都绑定方法，可以给class绑定方法：

def set_score(self, score):
    self.score = score


Student.set_score = set_score

s = Student()
s.set_score(100)
print(s.score)


# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：

class Student(object):
    __slots__ = ('name', 'age')


s = Student()
s.name = "kobe"
s.age = 40


# s.score=100  报错 因为限制只有name age属性
# 对继承的子类是不起作用的

class A(Student):
    pass


a = A()
a.score = 100
print(a.score)


class Student(object):
    def get_score(self):
        return self._score

    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError("score must be an integer!")
        elif score < 0 or score > 100:
            raise ValueError("score must between 0 ~ 100!")
        self._score = score


s = Student()
s.set_score(99)
print(s.get_score())


# s.set_score(101)


# 还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的


class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise ValueError("score must be an integer!")
        elif score < 0 or score > 100:
            raise ValueError("score must between 0 ~ 100!")
        self._score = score


s = Student()
s.score = 99
print(s.score)

# @property装饰器就是负责把一个方法变成属性，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值,而且设置的参数必须是私有属性
print(isinstance(s.score, classmethod))
print(isinstance(s.score, int))
print(isinstance(s.score, MethodType))


class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birthInfo(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth


s = Student()
s.birthInfo = 33
s.birthInfo = 44
print(s.birth)
print(s.age)

print("-----------------------------------------")


class Screen(object):
    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, value):
        self._width = value

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return 100


screen = Screen()
screen.height = 99
screen.width = 88
print(screen.width)
print(screen.height)
print(screen.resolution)
