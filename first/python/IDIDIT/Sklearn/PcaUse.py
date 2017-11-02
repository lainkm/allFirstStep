from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def main():
	data = load_iris()
	# print(data)
	X = data.data
	y = data.target
	pca = PCA(n_components = 2)
	reduce_X = pca.fit_transform(X)
	print(X, y, reduce_X)
	print(pca.fit(X).components_)
	x1, y1 = [], []
	x2, y2 = [], []
	x3, y3 = [], []
	for i in range(len(y)):
		if y[i] == 0:
			x1.append(reduce_X[i, 0])
			y1.append(reduce_X[i, 1])
		if y[i] == 1:
			x2.append(reduce_X[i, 0])
			y2.append(reduce_X[i, 1])
		if y[i] == 2:
			x3.append(reduce_X[i, 0])
			y3.append(reduce_X[i, 1])
	plt.scatter(x1, y1, c = 'r', marker = 'x')
	plt.scatter(x2, y2, c = 'b', marker = 'D')
	plt.scatter(x3, y3, c = 'g', marker = '.')
	plt.show()


if __name__ == '__main__':
	main()