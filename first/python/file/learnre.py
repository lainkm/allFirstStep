#正则表达式
# import re
# regex = re.compile(r'py.*?n')
# match = re.search(regex, 'pyddsnajhdn')
# print(match.group(0))

#淘宝接口处理和翻页
#查看淘宝搜索界面的url
#第一页：https://s.taobao.com/search?q=%E6%89%8B%E6%9C%BA&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20170929&ie=utf8
#第二页：https://s.taobao.com/search?q=%E6%89%8B%E6%9C%BA&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20170929&ie=utf8&p4ppushleft=5%2C48&s=48
#第三页：https://s.taobao.com/search?q=%E6%89%8B%E6%9C%BA&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20170929&ie=utf8&p4ppushleft=5%2C48&s=96

import requests
import re
import pandas as pd

def getHtml(url):
	try:
		r = requests.get(url, timeout = 30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""

def parsePageSaveAsList(lst, html):
	try:
		priceList = re.findall(r'\"price\"\:\"[\d\.]*\"', html)
		titleList = re.findall(r'\"title\"\:\".*?\"', html)
		for i in range(len(priceList)):
			price = eval(priceList[i].split(':')[1])  #按照：分隔成两部分[0]是price，[1]是价格，eval去掉引号
			title = eval(titleList[i].split(':')[1])
			lst.append([title, price])
	except:
		print("")


def SaveAsCsv(lst):
	title = ['手机', '价格']
	df = pd.DataFrame(lst, columns = title)
	df.to_csv('C2_taobaoList.csv', encoding = 'utf-8')

def main():
	search = '手机'
	page = 3
	surl = 'https://s.taobao.com/search?q=' + search
	searchList = []
	for p in range(page):
		try:
			url = surl + '&s=' + str(48 * p)   #从0开始
			html = getHtml(url)
			parsePageSaveAsList(searchList, html)
		except:
			continue
	print(len(searchList))
	SaveAsCsv(searchList)
main()