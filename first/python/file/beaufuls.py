from bs4 import BeautifulSoup
import requests

#获取这个demo页面
url = "https://python123.io/ws/demo.html"
r = requests.get(url)
print(r.status_code)
#print(r.text)
demo = r.text
soup = BeautifulSoup(demo, "html.parser") #对demo进行html的解析
#print(soup.prettify())

#bs4用法栗子：
soup1 = BeautifulSoup("<p>nihao</p>", "html.parser") #''与""没区别。。
#print(soup1.prettify())

#BeautifulSoup解析器
#html.parser  -->需要安装bs4
#xml 和lxml -->需要pip install lxml
#html5lib  -->pip install html5lib

#BeautifulSoup类的基本元素

print(soup.title)
print(soup.a.name)
print(soup.a.parent.name)
print(soup.a.parent.parent.name)
tag = soup.a    #标签a
print(tag.attrs)   #标签属性
print(tag.attrs['class'])  #因为属性是字典可以通过字典的方式访问
print(tag.attrs['href'])
print(type(tag.attrs))    #打印属性的类型，结果是dict列表 
print(type(tag))    #tag的类型











