#前五页排名，保存为csv文件
import requests
from bs4 import BeautifulSoup
import bs4
import csv    #单行读入
import pandas as pd   #整个读入
import codecs

def getHTML(url):
	try:
		r = requests.get(url, timeout = 30)
		r.raise_for_status()
		#print(r.status_code)
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""

def getInfoSaveAsList(printTitle, ulist, html):
	soup = BeautifulSoup(html, "html.parser")
	#print(soup.find('table'))

	for tr in soup.find('table').children:
		if isinstance(tr, bs4.element.Tag):
			tds = tr('td')
			if tds[0].string != 'Rank':
				ulist.append([tds[0].string, tds[1].string, tds[2].string])
			else:
				if printTitle == 1:
					ulist.append([tds[0].string, tds[1].string, tds[2].string])
	#print(ulist[:20])

def printList(ulist, num):
	for i in range(num):
		u = ulist[i]
		print("{:^6}\t{:^20}\t{:^6}".format(u[0], u[1], u[2]))


def findRankOf(ulist, name):
	for u in range(len(ulist)):
		if name in ulist[u]:
			return ulist[u][0]

def saveAsCsv(ulist):
	#使用csv库写入，但会多一行，一种办法是newline='',另一种办法是wb二进制什么的
	with open('C1_hduRankList(import_csv).csv', 'w', encoding ='utf-8', newline = "") as cf:
		writer = csv.writer(cf)
		# writer.writerow(ulist[1])  #写入一行(如表头)
		writer.writerows(ulist)     #写入多行

	df = pd.DataFrame(ulist[1:], columns = ulist[0])
	df.to_csv('C1_hduRankList(import_pandas).csv', encoding = 'utf-8')

def main():
	ulist = [] 
	
	for p in range(5):
		url = "http://acm.hdu.edu.cn/contests/contest_ranklist.php?cid=781&page="
		printTitle = p + 1
		html = getHTML(url + str(p + 1))
		getInfoSaveAsList(printTitle, ulist, html)
	# printList(ulist, len(ulist))
	# name = input("请输入要查询的名字:\n")
	# print(findRankOf(ulist, name))
	saveAsCsv(ulist)

main()