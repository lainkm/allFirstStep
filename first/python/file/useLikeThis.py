#打开py文件，读出每一行加上行号，写进一个txt文件
with open('useLikeThis.py', 'r', encoding = 'utf-8') as pyfile:
	cLine = pyfile.readlines()
	for line in range(len(cLine)):
		cLine[line] = str(line + 1) + ' ' + cLine[line]

with open('saveUseLikeThis.txt', 'w', encoding = 'utf-8') as txtfile:
	txtfile.writelines(cLine)