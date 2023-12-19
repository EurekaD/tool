"""
time_gap 计算时间和一个固定的时间点的 间隔
"""


import pandas as pd
from pandas import DataFrame
from TimeData_Process.re_process_time import time_re


def time_gap(df_time: DataFrame, start_time: str):
    df_time = pd.to_datetime(df_time, format='%Y/%m/%d')
    start_time = pd.to_datetime(start_time)
    gap = df_time - start_time

    # 返回一个序列 series
    return gap.dt.days


if __name__ == '__main__':
    df = pd.read_excel(r'C:\Users\RZ\OneDrive\桌面\test.xlsx')

    df = time_re(df, colume_name='time', inplace=True)

    gap = time_gap(df['time'], '2023/1/1')


