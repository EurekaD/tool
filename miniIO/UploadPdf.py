"""
上传数据到minIO,需要有数据的详细地址
MinioClient.py是我修改的easy版本
MinioClient_dai.py是原始的，爬虫里用的
"""
import math
import os.path

import pandas as pd
from minio import InvalidResponseError

from MinioClient import MinIOUtil

excel_path = r"C:\Users\RZ\OneDrive\桌面\2024大选详细网页\new\new.xlsx"
bucket_name = 'polldetail'

# df = pd.read_excel(excel_path)
upload_MinIO = MinIOUtil()

# 读取整个Excel文件
# excel_path = r'C:\Users\RZ\OneDrive\桌面\2024大选详细网页\3\3.xlsx'
excel_file = pd.ExcelFile(excel_path)

# 遍历每个sheet并读取为DataFrame，然后进行修改
for sheet_name in excel_file.sheet_names:
    df = excel_file.parse(sheet_name)
    print('sheet_name: ' + sheet_name)
    for index, row in df.iterrows():
        # 做一个判断， 如果表中没有 volume ,即没有对应上的， 不需要上传
        if math.isnan(row['volume']):
            continue

        file_path = os.path.join("C:/Users/RZ/OneDrive/桌面/2024大选详细网页/new/", row['url'])
        print(file_path)

        try:
            pdf_url = upload_MinIO.pdf_local_upload(file_path, bucket_name, use_uuid=True)
            if pdf_url is not None:
                print('上传成功: ' + pdf_url)
                df.loc[index, 'pdf_url'] = pdf_url
        except FileNotFoundError as err:
            print(err)

    with pd.ExcelWriter(excel_path, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name=sheet_name, index=False)

# 生成poll_detail
poll_detail = pd.DataFrame(df.loc[:, ['url', 'pdf_url', 'volume']])
poll_detail['url'] = poll_detail['url'].str[:-4]
poll_detail.rename(columns={'url': 'file_name', 'pdf_url': 'url'}, inplace=True)
poll_detail.to_excel('poll_detail_3_2.xlsx')
