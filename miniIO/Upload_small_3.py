import pandas as pd
from minio import InvalidResponseError
from Tools.OpenccUtils import ctozhLite
from MinioClient import MinIOUtil

excel_path = r"C:/Users/RZ/OneDrive/桌面/xm_regin_year_info.xlsx"
bucket_name = 'xmunews'
excel_file = pd.ExcelFile(excel_path)
df = excel_file.parse(sheet_name='all')
upload_MinIO = MinIOUtil()

for index, row in df.iterrows():
    print(index)
    if type(row['file_name']) is str:
        print(row['file_name'])
        image_path = row['file_name']
        url = upload_MinIO.img_local_upload(image_path, bucket_name)
        row['image'] = url
        df.loc[index] = row

df.to_excel('xm_regin_year_info.xlsx')
