import pandas as pd


# df = pd.read_excel("C:/Users/RZ/OneDrive/桌面/2024立委候选名单_V3.xlsx")
excel_file = pd.ExcelFile("C:/Users/RZ/OneDrive/桌面/2024立委候选名单_V3.xlsx")
df = excel_file.parse(sheet_name='区域立法委员')
df = pd.DataFrame(df)
df[['地区', '选区']].fillna(method='ffill').to_excel('fill.xlsx')
