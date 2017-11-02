# 服务器
import socket
 s = socket.socket()
 host = socket.gethostname()
 post = 12345
 s.bind((host, port))
 s.listen()
 while True:
 	c, addr = s.accept()
 	print('连接地址', addr)
 	c.send('')


# 客户端
import socket
s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))
print(s.recv(1024).decode())
s.close()
