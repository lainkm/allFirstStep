from sklearn import cluster
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt 
# import math

def main():

	# 数据预处理，得到上网开始时间和上网时长的X
	with open('学生月上网时间分布-TestData.txt',encoding='utf-8') as f:
		lines = f.readlines()
	mac2id = dict()
	onlineTimes = []
	for line in lines:
		fields = line.split(',')
		mac = fields[2]
		startTime = int(fields[4].split(' ')[1].split(":")[0])
		onlineTime = float(fields[6])
		# print(fields)
		# print(mac)
		# print(startTime)
		# print(onlineTime)

		# 去重
		if mac not in mac2id:
			mac2id[mac] = len(onlineTimes)           # 记录onlineTimes下标
			onlineTimes.append((startTime, onlineTime))
		else:
			onlineTimes[mac2id[mac]] = [(startTime, onlineTime)]

	# print(onlineTimes)
	X = np.array(onlineTimes).reshape(-1, 2)       # (-1全部)行数不知道，想变成2列
	# print(X)


	# 
	#
	# 得到data，进行训练,用上网开始时间进行聚类
	alg_db = cluster.DBSCAN(eps = 0.01, min_samples = 20)
	data = X[:,0:1]
	print(data)
	print()
	alg_db.fit(data)
	
	# 信息打印
	print(alg_db.labels_)
	labels = alg_db.labels_
	noise_ratio = len(labels[labels[:] == -1]) / len(labels)
	print("噪音比例为：",noise_ratio)

	print(set(labels))
	print(np.unique(labels))
	n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
	print("聚簇中心个数：", n_clusters_)
	# 打印各个簇的信息：
	for i in range(n_clusters_):
		print("聚簇",i,":")
		print((data[labels == i]).flatten())
		# print((data[labels == i]))


	# 用上网时长进行聚类，
	# 画出hist图，发现原数据不适合聚类
	# 进行取对数，调整后训练
	
	# plt.hist(X[:, 0],24)
	# plt.show()
	# plt.hist(X[:, 1])
	# plt.show()
	data2 = X[:, 1:]
	# print(data2.dtype)
	mask = (data2!=0)
	data2[mask] = np.log(data2[mask])
	# print(data2)
	# plt.hist(data2)
	# plt.show()

	# 训练
	db = cluster.DBSCAN(eps = 0.14,min_samples = 10)
	db.fit(data2)
	labels = db.labels_
	print(labels)



if __name__ == '__main__':
	main()