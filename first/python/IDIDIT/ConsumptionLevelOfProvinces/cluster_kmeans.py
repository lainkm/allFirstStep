# data：省份 + 8个不同方面的消费花销
# 要根据这8个特征用k-means进行聚类，划分消费水平
# 

from sklearn import cluster
import numpy as np 
import pandas as pd


def loadData(filePath):
	with open(filePath, 'r+') as f:
		lines = f.readlines()
	Data = []
	CityName = []
	for line in lines:
		item = line.strip().split(",")
		# print(item[0])
		CityName.append(item[0])
		# print(CityName)
		Data.append([float(item[i]) for i in range(1,len(item))])
	return Data, CityName

def main():
	data, cityName = loadData('31省市居民家庭消费水平-city.txt')
	# print(data)
	# print(cityName)
	alg = cluster.KMeans(n_clusters = 4)
	alg.fit_predict(data)
	# alg.fit(data)
	# alg.predict(data)
	expenses = np.sum(alg.cluster_centers_, axis = 1)

	print(alg.cluster_centers_)   # 每一个特征的的聚类中心的值
	print(expenses)

	print(alg.labels_)
	print(alg.inertia_)   # 评估聚簇个数是否合适，数越小越好
	# print()

	label = alg.labels_
	CityCluster = [[],[],[],[]]   # 写函数创建长度为n的空列表
	for i in range(len(label)):
		CityCluster[label[i]].append(cityName[i])
	# print(CityCluster)
	for i in range(len(CityCluster)):
		print('消费水平为 ', expenses[i], '的省份有：')
		print(CityCluster[i])


if __name__ == '__main__':
	main()
