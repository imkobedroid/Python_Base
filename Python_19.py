# 枚举
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print(Month.Jan)


class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)


# 动态的创建类  这和静态语言有非常大的不同，要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。


# 先定义函数
def fn(self, name='world'):
    print('Hello %s' % name)


# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
HelloClass = type("Hello", (object,), dict(hello=fn))  # 这里我们把函数fn绑定到方法名hello上。

print(HelloClass().hello())
