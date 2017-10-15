import unittest

from mydict import Dict

class TestDict(unittest.TestCase):

	#setUp为下面的测试统一处理一些东西，如打开数据库
	def setUp(self):
		print('打开数据库...')


	#测试Dict键值匹配，属于dict类型
	def test_init(self):
		d = Dict(a=1, b='test')
		self.assertEqual(d.a, 1)
		self.assertEqual(d.b, 'test')
		self.assertTrue(isinstance(d, dict))

	#测试键可以通过属性来访问
	def test_key(self):
		d = Dict()
		d['key'] = 'value'
		self.assertEqual(d.key, 'value')

	#测试属性设置同样作用于键
	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.assertEqual(d['key'], 'value')

	#测试访问不存在的key时，会抛出KeyError错误
	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(KeyError):
			value = d['empty']

	# 测试访问不存在的属性时， 会抛出AttributeError
	def test_attrerror(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty

	def tearDown(self):
		print('关闭数据库...')


# if __name__ == '__main__':
# 	unittest.main()
