import json

import requests

# 很多情况下的网站如果直接response.text会出现乱码的问题，所以这个使用response.content
# 这样返回的数据格式其实是二进制格式，然后通过decode()转换为utf-8，这样就解决了通过response.text直接返回显示乱码的问题.


a = requests.get('https://www.douban.com/')

print(a.status_code)
print(a.text)

r = requests.get('https://www.douban.com/search', params={'q': "python", 'cat': '1001'})
r.encoding = 'utf-8'
print(r.url)
print(r.encoding)
print(r.text)

print("--------------------------------------------------")

data = {
    "name": "zhaofan",
    "age": 22
}
response = requests.get("http://httpbin.org/get", params=data)
response.encoding = 'utf-8'
print(response.status_code)
print(response.url)
print(response.text)
print(response.headers)
print(response.encoding)

print("--------------------------------------------------")
response = requests.get('http://www.baidu.com')
response.encoding = 'utf-8'
print(response.headers)

print(response.content)  # 字节码额显示
# print(response.text)   #编码后的显示


response = requests.get("http://httpbin.org/get")
print(type(response.text))
print(response.json())
print(json.loads(response.text))
print(type(response.json()))

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
response = requests.get("https://www.zhihu.com", header=header)
print(response.text)

data = {
    "name": "zhaofan",
    "age": 21
}

response = requests.post('http://httpbin.org/post', data=data)
print(response.text)

# 图片上传
files = {"files": open("git.jpeg", "rb")}
response = requests.post("http://httpbin.org/post", files=files)
print(response.text)
