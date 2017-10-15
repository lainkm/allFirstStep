from bs4 import BeautifulSoup
import requests

#获取这个demo页面
url = "https://python123.io/ws/demo.html"
r = requests.get(url)
print(r.status_code)
#print(r.text)
demo = r.text
soup = BeautifulSoup(demo, "html.parser") #对demo进行html的解析
#print(soup.prettify())         #会加上换行符

#bs4用法栗子：
# soup1 = BeautifulSoup("<p>nihao</p>", "html.parser") #''与""没区别。。
# #print(soup1.prettify())

# #BeautifulSoup解析器
# #html.parser  -->需要安装bs4
# #xml 和lxml -->需要pip install lxml
# #html5lib  -->pip install html5lib

# #BeautifulSoup类的基本元素

# print(soup.title)
# print(soup.a.name)
# print(soup.a.parent.name)
# print(soup.a.parent.parent.name)
# tag = soup.a    #标签a
# print(tag.attrs)   #标签属性
# print(tag.attrs['class'])  #因为属性是字典可以通过字典的方式访问
# print(tag.attrs['href'])
# print(type(tag.attrs))    #打印属性的类型，结果是dict列表 
# print(type(tag))    #tag的类型

# #标签的内容string
# print(soup.a)
# print(soup.a.string)
# print(soup.p)
# print(soup.p.string)

# #处理注释，用类型判断是否是注释，比如a里面有注释，但是返回内容不显示是注释
# #这时需要看类型type(),看看类型是否是Comment
# print(soup.a.string)
# print(type(soup.a.string))

# #bs4基本使用
# print(soup.a)
# print(soup.a.name)   #名字就是a
# print(soup.a.attrs)   #属性
# print(soup.a.string)

#遍历
# print(soup.head)
# print(soup.head.contents)  #
# print(soup.body)
# print(soup.body.contents)
# print(len(soup.body.contents))

#遍历提取连接标签的连接地址
#find_all([属性列表]，属性值)
for link in soup.find_all('a'):    #返回列表类型也可以find_all(['a','b'])
	print(link.get('href'))
print(soup.find_all('p','course'))
print(soup.find_all(id = "link1"))
print(soup.find_all(id = "link"))


#正则表达式库,查找一b开头的标签的内容
import re
for tag in soup.find_all(re.compile('b')):
	print(tag.name)

print(soup.find_all(id = re.compile('link')))
print(soup(string = re.compile('Python')))







