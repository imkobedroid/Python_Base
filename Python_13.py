# 类
class Student(object):
    pass


bart = Student()
print(bart)

bart.name = "kobe"

print(bart.name)


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print("%s %s" % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


instance = Student("kobe", 40)
print(instance.name)
print(instance.score)

instance.print_score()
print(instance.get_grade())
