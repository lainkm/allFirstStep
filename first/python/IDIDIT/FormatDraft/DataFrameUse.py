import numpy as np
import pandas as pd 
from sklearn import datasets
import random as rm
import pandas.util.testing as tm

# X = datasets.load_iris()
# print(type(X.data))
# print(type(X.target))
# print(type(X))

# 时间索引
dates = pd.date_range('20171018', periods = 6)
# print(dates)
# print(type(dates))

# 创建特征名称
col = ['aa', 'bb', 'cc', 'dd']

# 创建df类型数据
df = pd.DataFrame(np.random.randn(6,4), index = dates, columns = col)
# print(df)
# print(type(df))

# 或者利用字典来创建, 长度不够自动填充或报错
df2 = pd.DataFrame({'A':np.random.randn(6), 'B':'b'})
# print(df2)
# print(type(df2))

# 调用DataFrame类型的信息
print(df.dtypes)
print(df.head())
print(df.tail())
print(df.index)
print(df.columns)  # 列名
print(df.values)   # 值
print(df.bb.values)
print(df['bb'].values)
print(df.describe())
print(df.info())
print(df.T)
print(df.sort_values(by='bb',ascending=False))  # 按某一行排序，默认ascending为True，升序
print(df.nlargest(5, columns = 'aa'))  # 返回前5个最大值
print(df)   # 而调用排序方法之后，本来的df是没有变的
df = df.sort_values(by='cc')
print(df) # 赋值之后才变了的
print(df.sort_index(axis = 0))   # 按行索引排序(默认)
print(df.sort_index(axis = 1))   # 按列索引排序


# 对df进行操作
# loc 用来选择数据
print(df.loc[dates[0]])  # 定位一行
print(df.loc[:, 'aa'])    # 定位一列
print(df.loc['20171018':'20171020', 'aa':'cc'])     # 用行列索引名定位一个区域
print(df.loc['20171021', 'cc'])  #定位一个(at[dates[1],'aa'], 和iat[1, 1]都行)
print(df.loc[df.cc.notnull(), 'cc'])  #定位一列中符合条件的所有的样本

# 用iloc使DataFrame想切片一样操作
print(df.iloc[1, 2])
print(df.iloc[1, 3: 5])

# 筛选
print('select')
print(df[df.aa>0])
print(df[(df.aa>0)&(df.cc>0)])  # 与
print(df[(df.aa>0)|(df.cc>0)])  # 或
print(df[['aa','bb']][(df.cc>0)|(df.dd>0)])  # 只要aabb两列，ccdd作为条件
alist = [-0.929618, -0.315837]
print(df['dd'].isin(alist))  # df[] = 赋值，df可以定位到dd属于alist里的值进行赋值


# 读取csv文件
# df = pd.read_csv('file.csv', encoding = 'gbk') # 有时候需要调整编码方式
print(df[:5])

