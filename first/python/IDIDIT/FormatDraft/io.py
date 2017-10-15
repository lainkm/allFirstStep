# f = open('C:\\Users\\heihei\\Desktop\\happy.txt','r');
# print(f.read(5))

# for line in f.readlines():
#     print(line.strip()) # 把末尾的'\n'删掉


# with open('..//Image//idenCode//03c77a54-af46-11e7-962a-3065ec8525bf.jpg', \
# 	'rb') as f:
# 	print(f.read(6))


import os
print(os.name)
# print(os.environ)
# print(os.environ.get('PATH'))
print(os.path.abspath('.'))
print(os.path.join(r'E:\allFirstStep\first\python\IDIDIT\FormatDraft','operFile'))
print(os.path.exists(r'E:\allFirstStep\first\python\IDIDIT\FormatDraft\operFile'))

#如果不存在就创目录，如果存在就删除
if os.path.exists(r'E:\allFirstStep\first\python\IDIDIT\FormatDraft\operFile'):
	os.rmdir(r'E:\allFirstStep\first\python\IDIDIT\FormatDraft\operFile')
else:
	os.mkdir(r'E:\allFirstStep\first\python\IDIDIT\FormatDraft\operFile')

#
