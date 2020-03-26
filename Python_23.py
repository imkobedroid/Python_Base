# StringIO和BytesIO


# StringIO顾名思义就是在内存中读写str。
import json
import pickle
from io import StringIO, BytesIO

f = StringIO()
f.write("hello")
f.write("   ")
f.write("python")

print(f.getvalue())

#######################################
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。


f = BytesIO()
f.write("hello world".encode('utf-8'))
print(f.getvalue())

# 序列化

# 可以随时修改变量，比如把name改成'Bill'，但是一旦程序结束，变量所占用的内存就被操作系统全部回收。如果没有把修改后的'Bill'存储到磁盘上，下次重新运行程序，变量又被初始化为'Bob'。
# 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
s = dict(name="kobe", age=40)
p = pickle.dumps(s)
print(p)

# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
address = "/Users/toushihiroshi/Desktop/python.txt"
try:
    f = open(address, 'wb')
    pickle.dump(s, f)  # 序列化保存到本地文件
finally:
    f.close()

with open(address, 'rb') as f:
    print(pickle.load(f))  # 反序列化到内存

# wb与w的区别是一个第一个是以二进制文件写入，第二个是文本写入
# rb与r的区别是第一个是读二进制，第二个是读取文本


# 序列化一般采用的是wb写入文件  rb读取然后然序列化到内存使用

address = "/Users/toushihiroshi/Desktop/python1.txt"
str1 = "测试写入字符串序列化"
try:
    f = open(address, 'wb')
    pickle.dump(str1, f)
finally:
    f.close()

with open(address, 'rb') as f:
    print(pickle.load(f))

# JSON
d = dict(name="kobe", age=40)
print(json.dumps(d))  # 序列化成json

d = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(d))  # 反序列化

# dumps是将dict转化成str格式，loads是将str转化成dict格式。
# dump和load也是类似的功能，只是与文件操作结合起来了


print("---------------------------------------------------------")


def student2dict(self):
    return {
        'name': self.name,
        'age': self.age
    }


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


s = Student('Bob', 20)
print(json.dumps(s, default=student2dict))
print(json.dumps(s, default=lambda k: k.__dict__))


# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。


# 同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例：
def dict2student(d):
    return Student(d['name'], d['age'])


json_str = '{"age": 10000, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))
print(json.loads(json_str, object_hook=dict2student).name)
print(json.loads(json_str, object_hook=dict2student).age)
