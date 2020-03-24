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
