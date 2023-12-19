import pandas as pd
from minio import InvalidResponseError
from Tools.OpenccUtils import ctozhLite
from MinioClient import MinIOUtil

bucket_name = 'xmunews'
upload_MinIO = MinIOUtil()

excel_file = pd.ExcelFile(r'C:\Users\RZ\OneDrive\桌面\xm_candidate_info-修正版 - 副本.xlsx')
df = excel_file.parse(sheet_name='Sheet2')

for index, row in df.iterrows():
    if type(row['image']) == float:
        print(row['name'])
        image_path = 'C:/Users/RZ/Pictures/立委大头照补充/' + row['name'] + '.jpg'
        url = upload_MinIO.img_local_upload(image_path, bucket_name)
        row['image'] = url
        print(image_path)
        df.loc[index] = row

df.to_excel('xm_candidate_info.xlsx')

