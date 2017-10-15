#打开py文件，读出每一行加上行号，写进一个txt文件
with open('useLikeThis.py', 'r', encoding = 'utf-8') as pyfile:
	cLine = pyfile.readlines()
	for line in range(len(cLine)):
		cLine[line] = str(line + 1) + ' ' + cLine[line]

with open('saveUseLikeThis.txt', 'w', encoding = 'utf-8') as txtfile:
	txtfile.writelines(cLine)

#map & reduce, reduce需要引入包
from functools import reduce
print(list(map(str, [1, 2, 3])))

def f(x):
	return x * x
print(list(map(f, [1, 2, 3])))

def a(x, y):
	return x * 10 + y
print(reduce(a, [1, 2, 3, 4]))

#利用map/reduce将字符转化成数字："9527"-->9527,简化为lambda函数
#但是python已经提供int函数了
def char2int(s):
	def fn(x, y):
		return x * 10 + y
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(fn, map(char2num, s))
print(char2int("9527"))
print(int("9527"))

#test首字母大写，map实现
def normalize(name):
    return name.capitalize()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#过滤器filter
#筛选出是偶数的
def is_odd(n):
	return n % 2 == 1
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

#筛选出不是空的
def not_empty(s):
	return s and s.strip()
print(list(filter(not_empty, ['A', 'B', None, 'c', ' '])))

#抓取网页requests库栗子
import requests
r = requests.get("http://baidu.com")
print('状态码:', r.status_code)
print(r.encoding)
#print(r.text)
r.encoding = 'utf-8'
#print(r.text)
print(type(r))

#get方法：r = requsets.get(url, params=None, **kwargs)
#来构造向服务器请求的Request对象
#返回一个含服务器资源的Response对象

#属性：
r.status_code #先检查这个。。返回200表示连接成功，其他为失败
r.text #url对应页面内容，即http响应内容的字符串形式
r.encoding #网页的编码方式，从httpheader中猜的方式？
r.apparent_encoding #从响应的内容文本中分析出的编码方式
r.content #如获得图片以二进制存储，通过content还原图片

#栗子：
#编码方式：网络上的资源有各种编码
#从http中header猜测编码方式，
#如果没有charset会默认为ISO-8859-1，这样的不能解析中文
r.encoding
#备选编码apparent_encoding是从内容分析的，所以r.encoding不能正确解码（乱码）的时候
#可以用apparent_encoding(如utf-8)赋予encoding，读取中文
r.encoding = 'utf-8'

#通用代码框架
#抓取网页并处理异常：
import requests
def getHTMLText(url):
	try:
		r = requests.get(url, timeout = 30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		"Error"

if __name__ == "__main__":
	url = "http://www.baidu.com"
	#print(getHTMLText(url))

#http协议：超文本传输协议，用户发起请求，服务器做出相应。
#采用url作为定位网络资源的标识
#url格式：
#HTTP协议对资源的操作：GET,HEAD,POST,PUT(所有url的资源都要提交),PATCH(局部更新),DELETE




#爬取网页Requests库
#爬取网站Scrapy库

#遵守robots协议
#打开网站根目录下的robots.txt看看
#http://www.baidu.com/robots.txt
#http：//www.jd.com/robots.txt

#实战一：
#爬取京东实战：
import requests
r = requests.get("https://item.jd.com/2967929.html")
print(r.status_code)
print(r.encoding)
print(r.request.headers)
#print(r.text)

#使用通用代码框架爬取京东商品信息：
import requests
url = "https://item.jd.com/2967929.html"
try:
	r = requests.get(url)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	#print(r.text[:1000])
except:
	print("爬取失败")

#实战二：
#爬取亚马逊,发现r.status_code不是200（网站可以通过约束User-Agent和robots协议拒绝访问？）
r = requests.get("https://www.amazon.cn/gp/product/B01M8L5Z3Y")
print(r.status_code)
print(r.encoding)
print(r.request.headers)   #发现头部信息中，爬虫发送的请求User-Agent如实的写了python..

#尝试修改头部信息，使User-Agent修改，如改为浏览器访问
kv = {'user-agent' : 'Mozilla/5.0'} #Mozilla-->浏览器
url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
r = requests.get(url, headers = kv)
print(r.status_code)
print(r.request.headers)

#框架形式：
import requests
url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
try:
	kv = {'user-agent':'Mozilla/5.0'}
	r = requests.get(url, headers = kv)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	#print(r.text[1000:2000])
except:
	print("爬取失败")

#实战三：
#搜索baidu关键词，同上只需要构造url就可以了，包含搜索的关键词
kv = {'wd':'Python'}
url = "http://www.baidu.com/s"   #baidu搜索的接口，搜索内容只需要修改wd=搜索内容的键值对
r = requests.get(url, params = kv)
print(r.status_code)
print(r.request.url)   #看一下url是否被构造成功
print(len(r.text))

#框架全代码：
import requests
url = "http://www.baidu.com/s"
try:
	kv = {'wd':'百度外卖'}
	r = requests.get(url, params = kv)
	print(r.request.url)   #对象的属性
	r.raise_for_status()
	print(len(r.text))  #特别长，就先别打印，看看长度
except:
	print("fail")

#实例四：
#网络图片的爬取和存储：
path = "E:/allFirstStep/first/python/file/jdPic.jpg"
url = "https://img14.360buyimg.com/n0/jfs/t9307/268/2052051657/217542/578f9944/59c72a7cN642b442e.jpg"
r = requests.get(url)
print(r.status_code)
#把二进制图片存成文件
with open(path, 'wb') as f:
	f.write(r.content)

#框架：
import requests
import os
url = "https://img14.360buyimg.com/n0/jfs/t9307/268/2052051657/217542/578f9944/59c72a7cN642b442e.jpg"
root = "E://allFirstStep//first//python//file//"
path = root + url.split('/')[-1]
try:
	if not os.path.exists(root):
		os.mkdir(root)
	if not os.path.exists(path):
		r = requests.get(url)
		with open(path, 'wb') as fp:
			fp.write(r.content)
			f.close()
			print("文件保存成功")
	else:
		print("文件已存在")
except:
	print("爬取失败")

#实例五
#随便查询下ip，找到url修改ip就好了
#提交的形式-->人工的分析接口
url = "http://www.ip138.com/ips138.asp?ip="
r = requests.get(url + '172.2.2.23')
print(r.status_code)
print(r.text[:500])   #不显示全，就前500这样就好


