import pandas as pd

"""
匹配两个 excel 中的值
"""


df = pd.read_excel("C:/Users/RZ/OneDrive/桌面/xm_candidate_info.xlsx")

df2 = pd.read_excel("C:/Users/RZ/OneDrive/桌面/xm_region_info.xlsx")




for index, row in df.iterrows():
    city = row['city']
    area = row['area']
    for index2, row2 in df2.iterrows():
        if city == row2['city'] and area == row2['area']:
            code = row2['code']
            row['code'] = code
            print(code)
            break
    df.loc[index] = row

df.to_excel('xm_candidate_info.xlsx')

