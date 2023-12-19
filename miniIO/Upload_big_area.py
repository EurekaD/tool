import pandas as pd
from minio import InvalidResponseError
from Tools.OpenccUtils import ctozhLite
from MinioClient import MinIOUtil

excel_path = r"选取地图_2.xlsx"
bucket_name = 'xmunews'

df = pd.read_excel(excel_path)
upload_MinIO = MinIOUtil()

for index, row in df.iterrows():
    if type(row['big_area']) is str:
        image_path = r"C:/Users/RZ/Pictures/立法委选举区域地图/big_area_process/" + row['big_area']
        url = upload_MinIO.img_local_upload(image_path, bucket_name)
        row['big_area'] = url
        df.loc[index] = row

df.to_excel('选举地图.xlsx')