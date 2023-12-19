"""
读取 excel 生成 点图
根据数据 近似曲线 得到曲线方程 
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from TimeData_Process.re_process_time import time_re
from TimeData_Process.time_math import time_gap

df = pd.read_excel(r'C:\Users\RZ\OneDrive\桌面\test.xlsx')
df = time_re(df, colume_name='time', inplace=True)
gap = time_gap(df['time'], '2023/1/1')
x = np.array(gap)
y = np.array(df['approval'])

plt.figure()


plt.scatter(x, y, color='r', marker='.', s=10)

plt.show()