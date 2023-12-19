import pandas as pd
from minio import InvalidResponseError
from Tools.OpenccUtils import ctozhLite
from MinioClient import MinIOUtil

excel_path = r"C:/Users/RZ/OneDrive/桌面/xm_candidate_info.xlsx"
bucket_name = 'xmunews'

df = pd.read_excel(excel_path)
upload_MinIO = MinIOUtil()

for index, row in df.iterrows():
    if type(row['image']) is str:
        image_path = row['image']
        url = upload_MinIO.img_local_upload(image_path, bucket_name)
        row['image'] = url
        df.loc[index] = row

df.to_excel('xm_candidate_info.xlsx')

