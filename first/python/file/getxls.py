#定向获取静态信息
#在网络上获取信息
#提取信息放入合适数据结构里
#输出数据
import requests
from bs4 import BeautifulSoup   #直接引得是bs4库里的BeatufulSoup类
import bs4

#从url获取网页信息
def getHTML(url):
	try:
		r = requests.get(url, timeout = 30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		#print(r.text[:500])
		return r.text
	except:
		return ""

#从html信息中提取数据存到list列表中
def getInfoSaveAsList(ulist, html):
	soup = BeautifulSoup(html, "html.parser")
	#print(soup.prettify()[:1000])
	cnt = 0
	for tr in soup.find('tbody').children:     #tbody列表中找到每一组tr标签
		if isinstance(tr, bs4.element.Tag):    #tr要的是标签信息，过滤掉不是标签类型的tr
			tds = tr('td')        #在列表中加入我们需要看到的td标签，如前三个
			cnt = cnt + 1         #这里查看源代码发现排名不是td标签出现的，而是tr里面的字符串。。。
			ulist.append([str(cnt), tds[1].string, tds[3].string])

def printList(ulist, num):
	tplt = "{0:^10}\t{1:{3}^10}\t{2:^6}"
	print(tplt.format("排名", "学校", "总分", chr(12288)))
	for i in range(num):
		u = ulist[i] 
		#print("{:^10}\t{:^6}\t{:^10}".format(u[0], u[1], u[2]))
		print(tplt.format(u[0], u[1], u[2], chr(12288)))


def main():
	uinfo = []
	url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html'
	html = getHTML(url)
	getInfoSaveAsList(uinfo, html)
	#print(uinfo[:20])
	printList(uinfo, 20)

main()
