import requests
import re
import csv
import traceback
from bs4 import BeautifulSoup

def getHtml(url, code = 'utf-8'):
	try:
		r = requests.get(url, timeout = 30)
		r.raise_for_status()
		r.encoding = code   #定向爬虫可以直接得到编码类型,再赋值
		return r.text
	except:
		return ""

def getStockList(lst, listUrl):
	html = getHtml(listUrl, 'BG2312')
	soup = BeautifulSoup(html, "html.parser")
	a = soup.find_all('a')
	for i in a:         #全页面有很多a标签，所以会有很多异常，try一下出现异常可能就不是我们要解析的范围
		try:
			href = 	i.attrs['href']
			lst.append(re.findall(r'[s][hz]\d{6}', href)[0])
		except:
				continue

def getStockInfo(lst, infoUrl, fpath):
	cnt = 0
	# headers = ['股票名称','最高', '最低', '今开', '昨收', '成交额', '成交量', '净值', '折价率']
	# with open('C3_stockList3.csv', 'a', encoding = 'utf-8',newline = "") as cf:
	# 	f_csv = csv.DictWriter(cf, headers)
	# 	f_csv.writeheader()		
	for istock in lst:
		html = getHtml(infoUrl + istock +'.html')
		try:
			if html == "":
				continue
			infoDict = {}
			soup = BeautifulSoup(html, "html.parser")
			sInfo = soup.find('div', attrs = {'class':'stock-bets'})
			name = sInfo.find_all(attrs = {'class':'bets-name'})[0]
			# price = sInfo.find_all(attrs = {'class':'price s-up'})[0]
			infoDict.update({'股票名称':name.text.split()[0]})
			
			keyList = sInfo.find_all('dt')
			valueList = sInfo.find_all('dd')
			for i in range(len(keyList)):
				key = keyList[i].text
				value = valueList[i].text
				infoDict[key] = value
			# with open(fpath, 'a', encoding = 'utf-8') as f:
			# 	f.write(str(infoDict) + '\n')
			# 	cnt = cnt + 1
			# 	print('\r当前速度：{:.2f}%'.format(cnt * 100 /len(lst), end=""))
			with open('C3_stockList3.csv', 'a', encoding = 'utf-8', newline = "") as cf:
				f_csv = csv.DictWriter(cf)
				# f_csv.writeheader()
				print(cnt)
				f_csv.writerow(str(infoDict))
				# for k, v in infoDict.iteritems():
				# 	writer.write([k, v])
		except:
		# 	cnt = cnt + 1
		# 	print('\r当前速度：{:.2f}%'.format(cnt * 100 /len(lst), end=""))
		# # traceback.print_exc()  #返回异常信息
			continue

def main():
	stock_list_url = "http://quote.eastmoney.com/stocklist.html"
	stock_info_url = "https://gupiao.baidu.com/stock/"
	output_file = "E://allFirstStep//first//python//IDIDIT//Crawler//C3_stockList.txt"
	slist = []
	getStockList(slist, stock_list_url)
	getStockInfo(slist, stock_info_url, output_file)

main()