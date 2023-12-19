"""
判断文件是否存在
"""

import pandas as pd

path1 = r"C:/Users/RZ/Pictures/选区图片/"

excel_path = r"C:/Users/RZ/OneDrive/桌面/xm_regin_year_info.xlsx"
excel_file = pd.ExcelFile(excel_path)
sheet_name = "2012"
df = excel_file.parse(sheet_name)

# df = pd.read_excel(excel_path)

list_file = []

# # 遍历输入文件夹中的所有文件
# for filename in os.listdir(path1):
#     list_file.append(filename[:-4])
#
# for index, row in df.iterrows():
#     name = row['name']
#     if name in list_file:
#         row['image'] = path1 + name + '.png'
#     df.loc[index] = row
#
# df.to_excel("xm_candidate_info_2012.xlsx")

# for filename in os.listdir(path1):
#     list_file.append(filename)
#
# for index, row in df.iterrows():
#     name = row['name']
#     for filename in list_file:
#         if name == filename[:-4]:
#             row['image'] = path1 + filename
#             break
#     df.loc[index] = row
#
# df.to_excel("xm_candidate_info.xlsx")