


import math
import os.path

import pandas as pd
from minio import InvalidResponseError
from Tools.OpenccUtils import ctozhLite
from MinioClient import MinIOUtil

excel_path = r"C:\Users\RZ\OneDrive\桌面\大事记录.xlsx"
bucket_name = 'xmunews'

df = pd.read_excel(excel_path)
upload_MinIO = MinIOUtil()

for index, row in df.iterrows():
    image_path = row['image']
    url = upload_MinIO.img_local_upload(image_path, mid_path='LegislativeElection/dsj/', bucket_name=bucket_name)
    row['image'] = url
    row['title'] = ctozhLite(row['title'])
    row['detail_info'] = ctozhLite(row['detail_info'])

    df.loc[index] = row

df.to_excel('大事记_入库.xlsx')
