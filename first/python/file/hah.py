import types
from types import MethodType

#创建一个类
class student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score

#变量名前面两个下划线表示私有变量
class Student(object):
	def __init__(self, name, score):
		self.__name = name
		self.__score = score
#		  __score__类外可访问，_score类外可访问最好不要访问，
#		  __score私有变量类外不可访问，当仍可以用_Student_name访问

	def get_name(self):
		return self.__name

	def get_score(self):
		return self.__score

	def set_name(self, name):
		self.__name = name

	#在set时候，可以做参数的检查，避免参数的无效性
	def set_score(self, score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('illegal score')

	# 通过len(对象名)直接调用
	def __len__(self):
		return len(self.__name) + len(str(self.__score))

def fn():
	pass

class stu():
	pass

def set_age(self, age):
	self.age = age

def set_no(self, no):
	self.no = no

#可控属性：把方法变成属性
class Animal():

	#定义可以getter，setter的方法属性
	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError("score must be an integer!")
		if value < 0 or value > 100:
			raise ValueError("score must between 0~100!")
		self._score = value

	#定义只读属性
	@property
	def birth(self):
		return self._brith

	@birth.setter
	def birth(self, value):
		self._birth = value

	@property
	def age(self):
		return 2015 - self._birth


def m():
	s1 = student("hhahda", 15)
	print(s1.name)

	s2 = Student("Dattt", 23)
	# print(s2.__name) 私有变量，类外不能访问了
	print(s2.get_name())
	print(s2.get_score())
	print(type(fn))
	print(type(abs))
	print(type(i for i in range(4)))
	print(len(s2))
	#判断是不是函数用types常量

	stu.set_age = set_age
	s = stu()
	s.set_age(1)
	print(s.age)

	ss = stu()
	ss.set_no = MethodType(set_age, stu)
	# s.set_no(2) 报错


if __name__ == "__main__":
	m()

# Case 1:

# 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。

# 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

# 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：

# sum up: __score__类外可访问，_score类外可访问最好不要访问，
#		  __score私有变量类外不可访问，当仍可以用_Student_name访问

# Case 2:

# 动态语言，将A类传入有run方法的类，只要传入的类有一run方法就行了，
# 而静态语言要求必须，需要传A类，则必须传入A类或其子类就可以了