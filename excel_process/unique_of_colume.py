import pandas as pd

"""
输出不唯一值
"""

df = pd.read_excel("C:/Users/RZ/OneDrive/桌面/xm_candidate_info.xlsx")

print(df['party'].unique())
