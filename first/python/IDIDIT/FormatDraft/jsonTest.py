
import json
d1 = json.dumps(d) #python转化为json语言(utf-8)所以能正确的转变
print(d1)      
print(json.loads(d1))  #json语言再变回来

print('\n')
#把类变成json语言
class Stu():
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score

class Tea():
	def __init__(self, name, age, score, no):
		self.name = name
		self.age = age
		self.score = score
		self.no = no

def Stu2Dict(std):
	return {
		'name': std.name,
		'age': std.age,
		'score': std.score
	}

def Dict2Stu(d):
    return Stu(d['name'], d['age'], d['score'])

s = Stu('a', 12, 99)
s1 = Stu('b', 12, 99)
t = Tea('c', 12, 99)
t1 = Tea('d', 12, 99)


# print(json.dumps(s, default = Stu2Dict))
#可以用lambda将所有的类都能使用这个
# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。
# 也有少数例外，比如定义了__slots__的class。
print(json.dumps(s, default = lambda obj: obj.__dict__))
print(json.dumps(s1, default = lambda obj: obj.__dict__))
print(json.dumps(t, default = lambda obj: obj.__dict__))
print(json.dumps(t1, default = lambda obj: obj.__dict__))

