from sklearn import datasets

x1 = datasets.load_boston()
x2 = datasets.load_iris()
x3 = datasets.load_diabetes()
x4 = datasets.load_digits()
x5 = datasets.fetch_olivetti_faces()
# x6 = datasets.fetch_20newsgroups()
# x7 = datasets.fetch_lfw_people()
# x8 = datasets.fetch_rcv1()

# boston房价 回归
print(x1.data.shape)
print(x1.target.shape)
print(x1.data)
print(x1.target)

# 鸢尾花，分类
print(x2.data.shape)
print(x2.target.shape)
print(list(x2.target_names))  # 分类 打印分类名称(3个)
print(x2.data)
print(x2.target)   # 0 1 2

# 糖尿病数据集 回归
print(x3.data.shape)
print(x3.target.shape)

# 手写数字数据集 分类
print(x4.data.shape)        # 每一维作为一个特征
print(x4.target.shape)      # 分类结果 0到9
print(x4.target_names)
print(x4.images.shape)      # 图像是8*8
import matplotlib.pyplot as plt
plt.matshow(x4.images[0])
plt.matshow(x4.images[1])
plt.matshow(x4.images[1796]) #画图
plt.show()

# 人脸图像
print(x5.data.shape)
print(x5.target.shape)
print(x5.images.shape)
import matplotlib.pyplot as plt
plt.matshow(x5.images[0])
plt.matshow(x5.images[399])
plt.show()

# 新闻分类
# print(x6.shape)
# print(x6.data.shape)
# print(x6.target.shape)
# print(x6)

# print(x7.shape)
# print(x8.shape)
