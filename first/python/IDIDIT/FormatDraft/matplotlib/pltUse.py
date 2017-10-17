# import matplotlib.pyplot as plt


# plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
# # 标签
# labels='青蛙','猪','狗','木头'
# # 标签对应的值(自动计算配比)
# sizes=15,20,45,10
# # 每一块颜色
# colors='yellowgreen','gold','lightskyblue','lightcoral'
# # pie是否分离开，分离的配比
# explode=0,0.1,0,0
# # 画图
# plt.pie(sizes,explode=explode,labels=labels,colors=plt.colors(),\
# 	autopct='%1.1f%%',shadow=True,startangle=50)
# # 形状
# plt.axis('equal')

# plt.show()
 
import numpy as np
import matplotlib.pyplot as plt
# from pylab import *
 
# x = np.arange(-5.0, 5.0, 0.02)
# y1 = np.sin(x)
 
# plt.figure()
# plt.subplot(211)
# plt.plot(x, y1)
 
# # plt.subplot(212)
# # #设置x轴范围
# # xlim(-2.5, 2.5)
# # #设置y轴范围
# # ylim(-1, 1)
# # plt.plot(x, y1)

# plt.subplot(212)
# plt.axis([-2.5, 2.5, -1, 1])
# plt.plot(x, y1)

# plt.show()

# t = np.arange(0., 5., 0.2)
 
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.show()

# import matplotlib.pyplot as plt
# plt.figure(1)                # 第一张图
# plt.subplot(211)             # 第一张图中的第一张子图
# plt.plot([1,2,3])
# plt.subplot(212)             # 第一张图中的第二张子图
# plt.plot([4,5,6])
 
 
# plt.figure(2)                # 第二张图
# plt.plot([4,5,6])            # 默认创建子图subplot(111)
 
# plt.figure(1)                # 切换到figure 1 ; 子图subplot(212)仍旧是当前图
# plt.subplot(211)             # 令子图subplot(211)成为figure1的当前图
# plt.title('Easy as 1,2,3')   # 添加subplot 211 的标题
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt

# # 高斯分布，均值是100，标准差是15
# mu, sigma = 100, 15
# x = mu + sigma * np.random.randn(10000)
 
# # 数据的直方图
# n, bins, patches = plt.hist(x, 50, normed=1, alpha=0.1)  # 第二个参数数值越大柱子越窄，alpha透明度

# plt.xlabel('Smarts')
# plt.ylabel('Probability') 
# plt.title('Histogram of IQ')  # 添加标题
# plt.text(60, .025, r'$mu=100, sigma=15$') # 添加文字, (位置，添加内容)
# plt.axis([40, 160, 0, 0.03]) # xy坐标范围
# plt.grid(True) #是否填充网格
# plt.show()

# #概率分布直方图  
# #高斯分布  
# #均值为0  
# mean = 0  
# #标准差为1，反应数据集中还是分散的值  
# sigma = 1  
# x=mean+sigma*np.random.randn(10000)  
# fig,(ax0,ax1) = plt.subplots(nrows=2,figsize=(9,6))  
# #第二个参数是柱子宽一些还是窄一些，越大越窄越密  
# ax0.hist(x,40,normed=1,histtype='bar',facecolor='yellowgreen',alpha=0.75)  
# ##pdf概率分布图，一万个数落在某个区间内的数有多少个  
# ax0.set_title('pdf')  
# ax1.hist(x,20,normed=1,histtype='bar',facecolor='pink',alpha=0.75,cumulative=True,rwidth=0.8)  
# #cdf累计概率函数，cumulative累计。比如需要统计小于5的数的概率  
# ax1.set_title("cdf")  
# fig.subplots_adjust(hspace=0.4)  
# plt.show()  

# import numpy as np
# import matplotlib.pyplot as plt
 
# ax = plt.subplot(111)
 
# t = np.arange(0.0, 5.0, 0.01)
# s = np.cos(2*np.pi*t)
# line, = plt.plot(t, s)
 
# plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
#             arrowprops=dict(facecolor='black', shrink=0.05),
#             )
 
# plt.ylim(-2,2)
# plt.show()



# 导入 matplotlib 的所有内容（nympy 可以用 np 这个名字来使用）
# from pylab import *
 
# # 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
# figure(figsize=(8,6), dpi=80)
 
# # 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
# subplot(1,1,1)
 
# X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
# C,S = np.cos(X), np.sin(X)
 
# # 绘制余弦曲线，使用蓝色的、连续的、宽度为 1 （像素）的线条
# plot(X, C, color="blue", linewidth=1.0, linestyle="-", label = "cos")
 
# # 绘制正弦曲线，使用绿色的、连续的、宽度为 1 （像素）的线条
# plot(X, S, color="r", lw=4.0, linestyle="-", label = "sin")
# legend(loc = 'upper left')
 
# plt.axis([-4,4,-1.2,1.2])
# # 设置轴记号
 
# xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
#        [r'$-pi$', r'$-pi/2$', r'$0$', r'$+pi/2$', r'$+pi$'])
 
# yticks([-1, 0, +1],
#        [r'$-1$', r'$0$', r'$+1$'])
# # 在屏幕上显示
# show()

# ax = gca()
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.spines['bottom'].set_position(('data',0))
# ax.yaxis.set_ticks_position('left')
# ax.spines['left'].set_position(('data',0))
# show()


# Import necessary packages
import pandas as pd
# %matplotlib inline
 
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from sklearn import datasets
# from sklearn import linear_model
from sklearn.linear_model import LinearRegression
import numpy as np
# Load data

# sklearn自带的数据集, 数据集data506行13列，label集target506列(需要用reshape变成m行1列)
# reshape
boston = datasets.load_boston()
print(boston.target.shape)
print(boston.data.shape)


yb = boston.target.reshape(-1, 1)
# print(yb)
Xb = boston['data'][:,5].reshape(-1, 1)
print(Xb[1:10, :])
# Plot data
plt.scatter(Xb,yb)
plt.ylabel('value of house /1000 ($)')
plt.xlabel('number of rooms')

# regr = linear_model.LinearRegression()
# regr.fit(Xb, yb)
alg = LinearRegression()
alg.fit(Xb, yb)

# Plot outputs
plt.scatter(Xb, yb,  color='black')
# plt.plot(Xb, regr.predict(Xb), color='blue',
         # linewidth=3)

plt.plot(Xb, alg.predict(Xb), color='blue',
         linewidth=3)
plt.show()

