"""
补充少量照片
直接读取文件上传
"""

import pandas as pd
from minio import InvalidResponseError
from Tools.OpenccUtils import ctozhLite
from MinioClient import MinIOUtil
import os

bucket_name = 'xmunews'
upload_MinIO = MinIOUtil()


# PATH = r'C:\Users\RZ\OneDrive\桌面\立委专项数据\人物信息收集\人物信息收集\人物照片_添加3'
# PATH = r'C:\Users\RZ\Pictures\立法委选举区域地图\张老师手工制作-补充缺失图片2'
# PATH = r'C:\Users\RZ\OneDrive\桌面\立委专项数据\人物信息收集\人物信息收集\人物照片_添加4_未添加的现任委员'
PATH = r'C:\Users\RZ\Pictures\立法委选举区域地图\张老师手工制作-补充缺失图片3'
PATH = r'C:\Users\RZ\OneDrive\桌面\画板 1.png'

imgs_path = os.listdir(PATH)
for img_path in imgs_path:
    print(img_path)
    full_img_path = os.path.join(PATH, img_path)
    # print(full_img_path)
    url = upload_MinIO.img_local_upload(full_img_path, bucket_name, 'LegislativeElection/regin_year_img_processed/')
    print(url)


