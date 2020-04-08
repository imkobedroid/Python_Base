# # 用来检测编码格式
# a = chardet.detect(b'Hello, world!')
# print(a)
#
# # 检测出的编码是ascii，注意到还有个confidence字段，表示检测的概率是1.0（即100%）。
#
# data = "离离原上草，一岁一枯荣".encode('gbk')
# a = chardet.detect(data)
# print(a)
#
# data = "离离原上草，一岁一枯荣".encode('utf-8')
# a = chardet.detect(data)
# print(a)
#
# print(data.decode('utf-8'))
#
import psutil

a = psutil.cpu_count()
print(a)

b = psutil.cpu_count(logical=False)
print(b)
# 2说明是双核超线程, 4则是4核非超线程


# 计CPU的用户／系统／空闲时间：
c = psutil.cpu_times()
print(c)
