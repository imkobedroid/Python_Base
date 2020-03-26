# 常用的内建模块


# 获取当前datetime
from datetime import datetime

print(datetime.now())

dt = datetime(2015, 4, 19, 12, 20)  # 用指定日期时间创建datetime
print(dt)
print(dt.timestamp())

s = 1429417200.0
print(datetime.fromtimestamp(s))

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

print(datetime.now().strftime('%a, %b %d %H:%M'))
