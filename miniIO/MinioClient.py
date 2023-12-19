# -*- coding: utf-8 -*-
# @File  : MinioClient.py
# @Author: chenlin
# @Date  : 2022/9/22 17:33
# @Desc  : 上传照片到OSS服务器
# 通过url匹配图片名称
import os
import re
import time
import uuid
from datetime import datetime
import io
import requests
from dateutil.relativedelta import relativedelta
from minio.error import InvalidResponseError
from local_connection import local_connection
# import yt_dlp

import datetime

class MinIOUtil:
    def __init__(self):
        self.minioClient = local_connection().minioClient
        self.minioUrl = local_connection().minioUrl


    def is_object_exist(self, bucket_name, img_name):
        exist = True
        try:
            self.minioClient.stat_object(bucket_name, img_name)
        except Exception as e:
            exist = False
        return exist

    def is_bucket_exist(self, bucket_name):
        # 判断Bucket是否存在，true：存在，false：不存在
        if self.minioClient.bucket_exists(bucket_name) == False:
            # 创建桶
            # self.minioClient.make_bucket(bucket_name, location="cn-north-1")
            print("桶 {} 不存在".format(bucket_name))
            return False
        else:
            return True

    def get_file_name(self, path):
        file_name = re.search(r'([^\\\/]*)\.pdf', path).group(1)
        print(file_name)
        return file_name

    def pdf_local_upload(self, path, bucket_name, use_uuid):
        """
        :param path: 本地pdf的路径
        :param bucket_name: 上传minio 桶名称
        :return: 返回上传公司服务器的图片路径
        """
        pdf_name = self.get_file_name(path) + '.pdf'
        is_exist = self.is_object_exist(bucket_name, pdf_name)

        if is_exist == False:
            # 读取本地图片为二进制流
            pdf_byte = open(path, 'rb').read()
            if use_uuid:
                pdf_name = str(uuid.uuid1()) + '.pdf'

            # 获取到图片二进制流实现io.RawIOBase的python对象
            pdf_data = io.BytesIO(pdf_byte)
            # 获取图片大小
            pdf_size = pdf_data.getbuffer().nbytes
            try:
                # 上传图片
                self.minioClient.put_object(bucket_name, pdf_name, pdf_data, pdf_size, content_type='application/pdf')
                result_url = self.minioUrl + bucket_name + "/" + pdf_name
                return result_url
            except InvalidResponseError as err:
                print(err)
        else:
            print("文件已存在")

    def img_local_upload(self, img_path, bucket_name, mid_path):
        """
        :param img_path: 上传图片的本地绝对路径
        :param bucket_name: 上传minio 桶名称
        :param mid_path: 中间的minIO上的文件夹路径 'LegislativeElection/candidate/'
        :return: 返回上传公司服务器的图片路径
        """
        # 读取本地图片为二进制流
        img_byte = open(img_path, 'rb').read()
        # 获取到图片二进制流实现io.RawIOBase的python对象
        img_data = io.BytesIO(img_byte)
        # 获取图片大小
        img_size = img_data.getbuffer().nbytes
        try:
            # 判断Bucket是否存在，true：存在，false：不存在
            if self.minioClient.bucket_exists(bucket_name) == False:
                # 创建桶
                self.minioClient.make_bucket(bucket_name, location="cn-north-1")

            file_extension = os.path.splitext(img_path)[1]

            # 在这里拼接名字，如果要体现出 MinIO上的路径，要在这里处理； 这里直接使用 uuid 造一个名字， 不去验证图片是否已经存在，一定可以上传
            img_name = mid_path + str(uuid.uuid1()) + file_extension

            print(img_name)
            self.minioClient.put_object(bucket_name, img_name, img_data, img_size, content_type='image/png')

            result_utl = self.minioUrl + bucket_name + "/" + img_name
            return result_utl
        except InvalidResponseError as err:
            print(err)


