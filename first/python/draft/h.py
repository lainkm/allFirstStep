import requests
from bs4 import BeautifulSoup
r = requests.get('https://book.douban.com/subject/27011961/')
soup = BeautifulSoup(r.text, 'lxml')
pattern = soup.find_all('p', 'comment-content')  #找到所有p标签，和属性名的列表
for i in pattern:
    print(i.string)



TCase = 1.756
for i in range(10):
    print('Case {0:3d}: {1:5d} '.format(i, int(TCase))) #:前数字表示参数的顺序，可以不加，使用默认正常对应的顺序
    print('Case {0:3d}: {1:5.2f} '.format(i, TCase)) #:后面表示类型说明符，5.3f指的是保留3位小数，占5个字符默认右对齐
    print('Case {:<3d}: {:5.2f} {{}}'.format(i, TCase)) #:<表示默认左对齐了
    TCase = TCase + 1



#处理文件
with open('stupid.py','r', encoding = 'utf-8') as fpy:
    cName = fpy.readlines()
    for line in range(0, len(cName)):
        cName[line] = str(line + 1) + ' ' + cName[line]

with open('stupid.txt', 'w', encoding = 'utf-8') as ftxt:
    ftxt.writelines(cName);

#function
def list_add1(L):
    L.append('END')
    return L

def list_add11(L):
    L.extend(['END'])

def list_add2(L = []):
    L.append('END')
    return L

def list_add3(L = None):
    if L is None:
        L = []
    L.append('END')
    return L

def calc(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum

def main():
    print(list_add1(['dasd','dasfa']))
    print(list_add1(['qwrrq']))
    print(list_add11(['asfag','fasf']))  #?
    print(list_add2())
    print(list_add3())
    print(list_add3())
    #abc全排列
    L = [a+b+c for a in 'abcd' for b in 'abcd' for c in 'abc' if a != b if a!= c if b != c]
    print(L)


main()