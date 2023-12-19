import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
from sklearn.linear_model import LinearRegression
import numpy as np
import tensorflow as tf
from matplotlib import rcParams
from sklearn.preprocessing import StandardScaler

tf.random.set_seed(42)

rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体
rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
matplotlib.use('TkAgg')

df = pd.read_excel('data.xlsx')

print(df.head())


def modol(X_train, y_train, X_test):
    # 构建简化的神经网络模型
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(5, activation='sigmoid', input_shape=(1,)),
        # tf.keras.layers.Dense(3, activation='sigmoid'),  # 隐藏层
        tf.keras.layers.Dense(3)  # 输出层，3个神经元对应3个预测值
    ])
    # 编译模型
    model.compile(optimizer='adam', loss='mean_squared_error')

    # 训练模型
    history = model.fit(X_train, y_train, epochs=200, batch_size=1)

    # 预测
    y_pred = model.predict(X_test)

    return y_pred


X_train = np.array(df['年份']).reshape(-1, 1)
y_train_0 = np.array(df['国民党']).reshape(-1, 1)
y_train_1 = np.array(df['民进党']).reshape(-1, 1)
y_train_2 = np.array(df['亲民党']).reshape(-1, 1)
y_train = np.array(df[['国民党', '民进党', '亲民党']]).reshape(-1, 3)
# X_test = np.append(X_train, [2024]).reshape(-1, 1)
X_test = np.array([i for i in range(1996, 2025)]).reshape(-1, 1)

# 数据标准化
X_train = X_train - 1995
X_test = X_test - 1995

y_pred = modol(X_train, y_train, X_test)


print("预测值:")
print(y_pred)
y_pred_0 = y_pred[:, 0]
y_pred_1 = y_pred[:, 1]
y_pred_2 = y_pred[:, 2]

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
