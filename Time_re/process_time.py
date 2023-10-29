import re
import pandas as pd
from pandas import DataFrame


def time_re(df_: DataFrame, colume_name: str, pattern: str, inplace: bool = False):
    df = df_
    for index, row in df.iterrows():
        match = re.match(pattern, row[colume_name])
        if match:
            df.loc[index, colume_name] = match.group(1)
            print('匹配到: ' + match.group(1))
        else:
            print('未匹配: ' + row[colume_name])
    df.to_excel('../../ML/MathAndML/result.xlsx', index=False)
    if inplace:
        return df



# '2021/7/27-8/1' -> '2021/7/27'
pattern = r'(\d{4}/\d{1,2}/\d{1,2})'


if __name__ == '__main__':
    excel_path = r'C:\Users\23145\Desktop\test.xlsx'
    df = pd.read_excel(excel_path)
    colume_name = 'time'
    time_re(df, colume_name, pattern)



