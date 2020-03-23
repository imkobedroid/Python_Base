# 继承与多肽


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def eat(self):
        print('Eating meat...')

    def run(self):
        print('dog is running...')


class Cat(Animal):
    def run(self):
        print('cat is running...')


class Test(object):
    def run(self):
        print(
            "静态语言 vs 动态语言:对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了")


dog = Dog()
dog.run()
dog.eat()
print(isinstance(dog, Animal))


# 多态

def run_twice(animal):
    animal.run()


run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Test())
