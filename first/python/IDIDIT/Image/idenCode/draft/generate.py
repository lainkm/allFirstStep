#coding=utf-8
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import string
import sys
import math

def randomChar():
	return chr(random.randint(65, 90))

def randomColor():
	return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def randomColor2():
	return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

def Type1():
	width = 60 * 4
	height = 60
	image = Image.new('RGB', (width, height), (255, 255, 255))
	#创建Font对象，其中字体文件在Windows\Fonts里面
	font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)
	# 创建Draw对象:
	draw = ImageDraw.Draw(image)
	# 填充每个像素:
	for x in range(width):
	    for y in range(height):
	        draw.point((x, y), fill=randomColor())
	# 输出文字:
	for t in range(4):
	    draw.text((60 * t + 10, 10), randomChar(), font=font, fill=randomColor2())
	# 模糊:
	image = image.filter(ImageFilter.BLUR)
	image.save('code.jpg', 'jpeg');

def Type2():
	fontPath = 'C:\Windows\Fonts\Arial.ttf'
	num = 4;
	size = (100, 30)
	bgcolor = (255, 255, 255)
	interferingLineColor = (255, 0, 0)
	drawLine = True
	lineNumber = (1, 5)
	w, h = size
	image = Image.new('RGBA', (w, h), bgcolor)
	font = ImageFont.truetype(fontPath, 25)
	draw = ImageDraw.Draw(image)

	#随机生成数字和字母
	source = list(string.ascii_letters) + list(string.digits)
	text = "".join(random.sample(source, 4))
	# 其他方法用ascii表转化，但是不如直接用常量
	# rndChr = list(chr(random.randint(65, 90)))+list(chr(random.randint(48, 57)))
	# text = "".join(random.sample(rndChr, 1))
	# print(text)


	fontColor = (0, 0, 255)
	font_w, font_h = font.getsize(text)
	draw.text(((w - font_w) / num, (h - font_h) / num),text, font= font,fill=fontColor) #填充字符串

	#随机绘制干扰线
	if drawLine:
		beginPoint = (random.randint(0, w), random.randint(0, h))
		endPoint = (random.randint(0, w), random.randint(0, h))
		draw.line([beginPoint, endPoint], fill = randomColor())

	#创建扭曲
	image = image.transform((w + 30, h + 10), Image.AFFINE, (1,-0.3,0,-0.1,1,0),Image.BILINEAR)
	image = image.filter(ImageFilter.EDGE_ENHANCE_MORE) #滤镜，边界加强
	image.save('idencode.png')

def Type3():
	pass

def main():
	Type1()
	Type2()
	print(list(string.ascii_letters)+ list(string.digits))
	print(list(chr(random.randint(65, 90)))+list(chr(random.randint(48, 57))))


	
main()