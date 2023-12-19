import pandas as pd

df = pd.read_excel(r"2020_立法委员选举结果.xls")

df['地區'] = df['地區'].fillna(method='ffill')

print(df.head())