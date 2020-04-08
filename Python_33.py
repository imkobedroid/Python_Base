import socket

# 端口号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用。

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect('www.sina.com.cn', 80)


# 新浪强制HTTPS协议访问 所以 80端口改443 socket 改 ssl
import threading
import time

# s = ssl.wrap_socket(socket.socket())
# s.connect(('www.sina.com.cn', 443))
#
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#
# # 接收数据:
# buffer = []
# while True:
#     # 每次最多接收1k字节:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)
# s.close()
#
# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
# # 把接收的数据写入文件:
# with open('sina.html', 'wb') as f:
#     f.write(html)

# 服务端


# 还可以用127.0.0.1绑定到本机地址。127.0.0.1是一个特殊的IP地址，表示本机地址
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('Waiting for connection...')


def tcpLink(socket, address):
    print('Accept new connection from %s:%s...' % address)
    socket.send(b'Welcome!')
    while True:
        data = socket.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        socket.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    socket.close()
    print('Connection from %s:%s closed.' % address)


while True:
    sock, address = s.accept()
    t = threading.Thread(target=tcpLink, args=(sock, address))
    t.start()

# 客户端
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
