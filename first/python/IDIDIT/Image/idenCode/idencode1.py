import sys
import math
import random
import string
from PIL import Image, ImageFont, ImageDraw, ImageFilter
from uuid import uuid1

def randomChar():
	source = list(string.ascii_letters) + list(string.digits)
	return random.sample(source, 1)

def randomPoint():
	Point = '.'
	return Point

def randomColor():
	return (random.randint(64, 255), \
		random.randint(64, 255), random.randint(64, 255))

def randomColorText():
	return (random.randint(32, 127), \
		random.randint(32, 127), random.randint(32, 127))

def randomSymbol():
	symbol = ['^','-', '~', '_', '.']
	return random.sample(symbol, 1)
	
def generate():
	#init
	fontPath = 'C:\Windows\Fonts\Arial.ttf'
	drawLine = True
	charNum = 4
	size = (60 * 3, 60)
	width, height = size

	#创建对象画图
	# image = Image.new('RGB', (width, height), randomColor()) #彩底
	image = Image.new('RGB', (width, height), (255, 255, 255)) #白底
	font = ImageFont.truetype(fontPath, 45)
	disFont = ImageFont.truetype(fontPath, 25)
	draw = ImageDraw.Draw(image)

	# 将白色背景色改为每个像素点填充
	# for i in range(width):
	# 	for j in range(height):
	# 		draw.point((i, j), fill = randomColor())

	# 将白色背景色改为每个像素填充
	for i in range(0, width, 2):
		for j in range(0, height, 5):
			draw.point((random.randint(0, width), random.randint(0, height)),\
				fill = (152, 245, 255))   #天蓝色背景点

	#生成四个字符
	idencode = ''
	for i in range(4):
		c = randomChar()[0]    #string类型的
		idencode = idencode+c
		# print(idencode)
		h = random.randint(1, height - 45)
		w = width  / 5 * i + 15
		draw.text((w, h), c, font = font, fill = randomColorText())
		#加四条有颜色的干扰线
		if drawLine:
			beginPoint = (random.randint(0, width), random.randint(0, height))
			endPoint = (random.randint(0, width), random.randint(0, height))
			draw.line([beginPoint, endPoint], fill = randomColor())

	print("保存验证码 {} 到数据库".format(idencode))

	#加干扰
	for i in range(0, width, 15):
		disturbing = randomSymbol()[0]
		disPoint = randomPoint()
		w = random.randint(1, width)
		h = random.randint(1, height)
		draw.text((w, h), disturbing, font = disFont,\
			fill = randomColorText())
		draw.text((w, h), disPoint, font = disFont,\
			fill = randomColorText())
		#加很多白色干扰线
		if drawLine:
			beginPoint = (random.randint(0, width), random.randint(0, height))
			endPoint = (random.randint(0, width), random.randint(0, height))
			draw.line([beginPoint, endPoint], fill = (255, 255, 255))

	# 创建扭曲 这个可以用的  = =
	# image = image.transform((width + 30, height + 10),\
	# 	Image.AFFINE, (1,-0.3,0,-0.1,1,0),Image.BILINEAR) 

	# image = image.filter(ImageFilter.EDGE_ENHANCE_MORE) #滤镜，边界加强
	# image.filter(ImageFilter.BLUR)  #滤镜 模糊

	# 用uuid1保存为随机码命名的图
	codeName = '{}.jpg'.format(uuid1())
	saveDir = './{}'.format(codeName)
	image.save(saveDir, 'jpeg')
	print('已保存的图片：{}'.format(saveDir))

if __name__ == "__main__":
	generate()