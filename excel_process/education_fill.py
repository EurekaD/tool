
"""
缺失值处理， 以前一个非空值来填充 method='ffill'
"""

import pandas as pd

df = pd.read_excel("C:/Users/RZ/OneDrive/桌面/xm_candidate_info.xlsx")

file = pd.ExcelFile("C:/Users/RZ/OneDrive/桌面/人物信息收集/2024立委候选名单_V3.xlsx")
df2 = file.parse(sheet_name='区域立法委员_学历')

# print(df2.head())
# print(df2.query("立法委员首选人姓名=='林岱桦'")[-1:])

# for index, row in df2.iterrows():
#     name = row['立法委员首选人姓名']
#     edu = row['学历名称']


for index, row in df.iterrows():
    name = row['name']
    education = df2.query("立法委员首选人姓名=='{}'".format(name))[-1:]["学历名称"]
    print(education)
    row['education'] = education
    df.loc[index] = row

df.to_excel("xm_candidate_info.xlsx")