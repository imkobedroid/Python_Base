# map
Student = {"kobe": 100, "dong": 200}
print(Student.get("kobe"))
print(Student["dong"])

print("kobe" in Student)
print("mac" in Student)

Student.pop("dong")
print(Student)

# set

Student = {1, 2, 3}
print(Student)
Student.add(4)
print(Student)
Student.remove(2)
print(Student)

s1 = {1, 2, 3}
s2 = {1, 2, 4}
print(s1 & s2)
print(s1 | s2)

a = ['c', 'b', 'a']
a.sort()
print(a)

# 不可变参数
a = "abc"
a.replace('a', 'A')
print(a)
b=a.replace('a', 'A')
print(b)
