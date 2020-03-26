# IO操作


try:
    address = "/Users/toushihiroshi/Desktop/错误日志.txt"
    f = open(address, 'r')
    # 标示符'r'表示读，这样，我们就成功地打开了一个文件。
    print(f.read())
finally:
    f.close()

# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：

with open(address, 'r') as f:
    print(f.read())
# 这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。


f = open(address, 'r')

for line in f.readline():
    print(line.split())  # 把末尾的'\n'删掉

f = open(address, 'r', encoding='gbk')

# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
f = open(address, 'r', encoding='gbk', errors='ignore')

# 写文件


address = "/Users/toushihiroshi/Desktop/python.txt"

with open(address, 'w') as f:
    f.write("hello python")

# 细心的童鞋会发现，以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入。
