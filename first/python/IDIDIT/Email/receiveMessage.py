import poplib
import logging
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
from datetime import datetime

logging.basicConfig(level=logging.INFO)


email = '1239842226@qq.com'
password = 'pyemyskkuoxigegj'
pop3_server = 'pop.qq.com'

# 连接到POP3服务器:
server = poplib.POP3(pop3_server)            # 同smtp一样 用qq是带ssl的
server = poplib.POP3_SSL(pop3_server, '995')

print(server.getwelcome().decode('utf-8'))

# 身份认证:
server.user(email)
server.pass_(password)

# stat()返回邮件数量和占用空间:
print('Messages: %s. Size: %s' % server.stat())
# list()返回所有邮件的编号:
resp, mails, octets = server.list()
# 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
print(mails)

# 获取最新一封邮件, 注意索引号从1开始:
index = len(mails)
resp, lines, octets = server.retr(index)

# lines存储了邮件的原始文本的每一行,
# 可以获得整个邮件的原始文本:
msg_content = b'\r\n'.join(lines).decode('utf-8')
# 稍后解析出邮件:
msg = Parser().parsestr(msg_content)

# 可以根据邮件索引号直接从服务器删除邮件:
# server.dele(index)
# 关闭连接:
server.quit()
