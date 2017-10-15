class Fib():
	def __init__(self):
		self.a = 1
		self.b = 1

	#可迭代输出
	def __iter__(self):
		return self

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b   #这里顺序。。
		if self.a > 1000:
			raise StopIteration()
		return self.a

	#可按list取出元素：(实现切片)
	def __getitem__(self, n):
		if isinstance(n, int):
			a, b = 1, 1
			for x in range(n):
				a, b = b, a + b
			return a
		if isinstance(n, slice):
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a + b
			return L


def gene_Fib():
	for i in Fib():
		print(i)

	print('\n',Fib()[10])

if __name__ == "__main__":
	gene_Fib()