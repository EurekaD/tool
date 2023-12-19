"""
匹配数据库中的字段到本地的excel中；
用在 马后炮 添加数据的时候，
具体的步骤是：
1.下载数据 pdf
2.匹配到已有的表中的字段，  volume 这个代码做的事情
3.上传到minIO，获取到url   pdf_url
4.获得匹配的字段volume和pdf_url之后，新建一张表，插入
"""

import pandas as pd
from db import DB


db = DB()

# 读取整个Excel文件
# excel_path = r'C:\Users\RZ\OneDrive\桌面\2024大选详细网页\3_2\3_2.xlsx'
excel_path = r'C:\Users\RZ\OneDrive\桌面\2024大选详细网页\new-4\new.xlsx'
excel_file = pd.ExcelFile(excel_path)

# 遍历每个sheet并读取为DataFrame，然后进行修改
for sheet_name in excel_file.sheet_names:
    df = excel_file.parse(sheet_name)
    print('sheet_name: ' + sheet_name)
    for index, row in df.iterrows():
        approval_rating = row['民进']
        no_know = row['no_know']
        print(('赖清德', approval_rating, no_know, no_know), end=' ')
        data = [('赖清德', str(approval_rating), str(no_know), str(no_know))]
        volume = db.matching_db(data)
        if volume is not None:
            print(volume[1])
            df.loc[index, 'volume'] = volume[1]
        else:
            print('未查询到对应的volume')

    # 储存到原来的excel中， 注意备份原表
    with pd.ExcelWriter(excel_path, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name=sheet_name, index=False)


# SELECT organization, volume FROM `vote_opinion_survey`
# WHERE name_candidate='赖清德' AND approval_rating='0.294' AND (no_know='0.215' OR undetermined_rating='0.215')

# data = [('赖清德', '0.294', '0.215', '0.215')]
# volume = db.matching_db(data)[1]
# print(volume)


