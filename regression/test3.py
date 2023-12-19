import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
from sklearn.linear_model import LinearRegression
import numpy as np
import tensorflow as tf
from matplotlib import rcParams
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor

tf.random.set_seed(42)

rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体
rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
matplotlib.use('TkAgg')

df = pd.read_excel('data.xlsx')

print(df.head())


def modol(X_train, y_train, X_test):
    # 创建决策树回归模型
    model = DecisionTreeRegressor(max_depth=3)
    # 拟合模型
    model.fit(X_train, y_train)
    # 进行预测
    predictions = model.predict(X_test)
    return predictions


def modol1(X_train, y_train, X_test):
    # 创建支持向量机回归模型
    model = SVR(kernel='linear')
    # 拟合模型
    model.fit(X_train, y_train)
    # 进行预测
    predictions = model.predict(X_test)
    return predictions


def modol2(X_train, y_train, X_test):
    # 创建K近邻回归模型
    model = KNeighborsRegressor(n_neighbors=3)
    # 拟合模型
    model.fit(X_train, y_train)
    # 进行预测
    predictions = model.predict(X_test)
    return predictions

X_train = np.array(df['年份']).reshape(-1, 1)
y_train_0 = np.array(df['国民党']).reshape(-1, 1)
y_train_1 = np.array(df['民进党']).reshape(-1, 1)
y_train_2 = np.array(df['亲民党']).reshape(-1, 1)
# X_test = np.append(X_train, [2024]).reshape(-1, 1)
X_test = np.array([i for i in range(1996, 2025)]).reshape(-1, 1)

# 数据标准化
scaler = StandardScaler()
X_train = X_train - 1995
X_test = X_test - 1995

y_pred_0 = modol2(X_train, y_train_0, X_test)
y_pred_1 = modol2(X_train, y_train_1, X_test)
y_pred_2 = modol2(X_train, y_train_2, X_test)

print("预测值:")
print(y_pred_0)
print(y_pred_1)
print(y_pred_2)

# 绘制原始数据和回归线
time_X = [1996, 2000, 2004, 2008, 2012, 2016, 2020]
time_pre = [i for i in range(1996, 2025)]

plt.scatter(time_X, y_train_0, color='blue')
plt.plot(time_pre, y_pred_0, color='blue', linewidth=2, label='国民党')
plt.scatter(time_X, y_train_1, color='green')
plt.plot(time_pre, y_pred_1, color='green', linewidth=2, label='民进党')
plt.scatter(time_X, y_train_2, color='yellow')
plt.plot(time_pre, y_pred_2, color='yellow', linewidth=2, label='亲民党')
plt.xlabel('时间')
plt.ylabel('得票率')
plt.title('线性回归预测')
plt.legend()
plt.show()