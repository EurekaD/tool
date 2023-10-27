# -*- coding: utf-8 -*-
# @File  : MinioClient_dai.py
# @Author: kangaroo
# @Date  : 2022/9/22 17:33
# @Desc  : 上传照片到OSS服务器
# 通过url匹配图片名称
import re
import time
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
        # self.minioClient = Minio('192.168.1.191:9000',
        #                          access_key='admin',
        #                          secret_key='admin123456',
        #                          secure=False)
        self.minioUrl = local_connection().minioUrl

    def isObjectExist(self, bucket_name, img_name):
        exist = "true"
        try:
            self.minioClient.stat_object(bucket_name, img_name)
        except Exception as e:
            exist = "false"
        return exist

    # 提取url名称
    def get_image_name(self, url):
        """
        :param url: 图片详细的url路径
        :return: 图片名称
        """
        pattern = re.search("([|.|\w|\s|-])*?.(jpg|gif|png|pdf)", url)
        if pattern is None:
            result = url + ".png"
            img_url = re.search("([|.|\w|\s|-])*?.(jpg|gif|png|pdf)", result)
            return img_url.group()
        image_name = pattern.group()
        return image_name

    # 定义一个proxy类
    def get_proxy(self):
        proxy = '127.0.0.1:7890'
        proxies = {
            'http': 'http://' + proxy,
            'https': 'http://' + proxy
        }

        return proxies

    # 定义视频上传方法结构两个参数：1.minio桶名称 2.视频标题 3.视频二进制流变量 4.视频大小 5.content_type
    # def video_Upload(self, videoUrl, bucket_name):
    #     """
    #     :param videoUrl: 视频详细url路径
    #     :param bucket_name: 上传minio 桶名称
    #     :video_title 视频标题
    #     :return: 返回上传公司服务器的图片路径
    #     """
    #     ydl_opts = {}
    #     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    #         # Use the extract_info method with the 'download=False' option to get the video information without downloading it
    #         info_dict = ydl.extract_info(videoUrl, download=False)
    #         # Get the video binary code by accessing the 'url' field of the 'formats' list in the info_dict
    #         # print(info_dict['formats'][-1]['url'])
    #         video_length = info_dict['duration_string']  # 视屏总长
    #         id = info_dict['id']  # 数据唯一id
    #         video_time = datetime.datetime.fromtimestamp(
    #             info_dict['timestamp'])  # 原始时间是字符串，使用datetime中的fromtimestamp方法 视频更新时间
    #         video_download_url = info_dict['formats'][-1]['url']
    #         # print(info_dict['formats'])
    #         # print("*" * 18)
    #         # print(video_download_url)
    #         try:
    #             # 判断Bucket是否存在，true：存在，false：不存在
    #             if self.minioClient.bucket_exists(bucket_name) == False:
    #                 # 创建桶
    #                 self.minioClient.make_bucket(bucket_name, location="cn-north-1")
    #             # 判断视频是否存在
    #             # isExist = self.isObjectExist(bucket_name, video_title)
    #             isExist = self.isObjectExist(bucket_name, "video/" + id + ".mp4")
    #             if isExist == "false":
    #                 proxies = self.get_proxy()
    #                 # 视频二进制文件
    #                 time.sleep(10)
    #                 # video_binary = io.BytesIO(
    #                 #     urllib.request.urlopen(info_dict['formats'][-1]['url'], timeout=10).read())
    #
    #                 video_binary_reponse = requests.get(url=video_download_url, stream=True,
    #                                                     proxies=proxies)
    #                 # 获取到视频二进制流实现io.RawIOBase的python对象。
    #                 video_binary = io.BytesIO(video_binary_reponse.content)
    #                 # 二进制大小
    #                 video_size = video_binary.getbuffer().nbytes
    #                 # Put the video binary to the bucket 'videos' with the name 'video.mp4'
    #                 self.minioClient.put_object(bucket_name, "video/" + id + ".mp4", video_binary, video_size,
    #                                             content_type='audio/mp4')
    #
    #             video_url = self.minioUrl + bucket_name + "/video/" + id + ".mp4"
    #             #print(video_url, video_length, video_time, video_download_url, id)
    #             return video_url, video_length, video_time, video_download_url, id
    #         except Exception as err:
    #             print(err.args)

    def videoImgUpload(self, url, bucket_name, key):
        """
        :param url: 图片详细url路径
        :param bucket_name: 上传minio 桶名称
        :key : 当前照片的唯一标识
        :return: 返回上传服务器的图片路径
        """
        # 获取图片名称
        img_name = key + str(self.get_image_name(url))

        try:
            # 判断Bucket是否存在，true：存在，false：不存在
            if self.minioClient.bucket_exists(bucket_name) == False:
                # 创建桶
                self.minioClient.make_bucket(bucket_name, location="cn-north-1")
            # 判断图片是否存在
            isExist = self.isObjectExist(bucket_name, "image/"+img_name)
            if isExist == "false":
                proxies = self.get_proxy()
                # 使用requests 请求url下载照片
                r = requests.get(url=url, stream=True, proxies=proxies)
                # 获取到图片二进制流实现io.RawIOBase的python对象。
                img_data = io.BytesIO(r.content)
                # 获取图片大小
                img_size = img_data.getbuffer().nbytes
                # 上传图片
                self.minioClient.put_object(bucket_name, "image/"+img_name, img_data, img_size, content_type='image/png')
            result_utl = self.minioUrl + bucket_name + "/image/" + img_name
            return result_utl
        except InvalidResponseError as err:
            print(err)

    # 定义图片上传方法接收两个参数：1.url 上传文件连接 ，2.bucket_name minio桶名称
    def imgUpload(self, url, bucket_name):
        """
        :param url: 图片详细url路径
        :param bucket_name: 上传minio 桶名称
        :return: 返回上传公司服务器的图片路径
        """
        # 获取图片名称
        img_name = self.get_image_name(url)

        try:
            # 判断Bucket是否存在，true：存在，false：不存在
            if self.minioClient.bucket_exists(bucket_name) == False:
                # 创建桶
                self.minioClient.make_bucket(bucket_name, location="cn-north-1")
            # 判断图片是否存在
            isExist = self.isObjectExist(bucket_name, img_name)
            if isExist == "false":
                proxies = self.get_proxy()
                # 使用requests 请求url下载照片
                r = requests.get(url=url, stream=True, proxies=proxies)
                # 获取到图片二进制流实现io.RawIOBase的python对象。
                img_data = io.BytesIO(r.content)
                # 获取图片大小
                img_size = img_data.getbuffer().nbytes
                # 上传图片
                self.minioClient.put_object(bucket_name, img_name, img_data, img_size, content_type='image/png')
            # 上传pdf文档
            # minioClient.fput_object('images', '技术要求.pdf',r'C:\Users\Administrator\Desktop\技术要求.pdf',content_type='application/pdf')

            result_utl = self.minioUrl + bucket_name + "/" + img_name
            return result_utl
        except InvalidResponseError as err:
            print(err)

    # 上传本地图片工具
    def imgLocalUpload(self, img_path, bucket_name):
        image_time = datetime.strftime(datetime.now() - relativedelta(months=1), "%Y-%m")
        # 获取图片名称
        img_name = re.findall('person_output\/(.*?)\.png', img_path)[0].replace(f'{image_time}',
                                                                                f'-{image_time}-词云.png')
        img_real_path = img_path.replace(f'{image_time}', f'-{image_time}-词云')
        # 读取本地图片为二进制流
        img_byte = open(img_real_path, 'rb').read()
        # 获取到图片二进制流实现io.RawIOBase的python对象
        img_data = io.BytesIO(img_byte)
        # 获取图片大小
        img_size = img_data.getbuffer().nbytes
        try:
            # 判断Bucket是否存在，true：存在，false：不存在
            if self.minioClient.bucket_exists(bucket_name) == False:
                # 创建桶
                self.minioClient.make_bucket(bucket_name, location="cn-north-1")
            # 判断图片是否存在
            isExist = self.isObjectExist(bucket_name, img_name)
            if isExist == "false":
                # 上传图片
                self.minioClient.put_object(bucket_name, img_name, img_data, img_size, content_type='image/png')
            result_utl = self.minioUrl + bucket_name + "/" + img_name
            return result_utl
        except InvalidResponseError as err:
            print(err)

    def pdfUpload(self, url, bucket_name):
        """

        :param url: pdf 详细路径
        :param bucket_name: 上传minio 桶名称
        :return: 返回上传公司服务器的文件路径
        """
        # 获取文件名称
        pdf_name = self.get_image_name(url)
        # 使用requests 请求url下载文件
        r = requests.get(url, stream=True)
        # 获取到图片二进制流实现io.RawIOBase的python对象。
        pdf_data = io.BytesIO(r.content)
        # 获取图片大小
        pdf_size = pdf_data.getbuffer().nbytes
        try:
            # 判断Bucket是否存在，true：存在，false：不存在
            if self.minioClient.bucket_exists(bucket_name) == False:
                # 创建桶
                self.minioClient.make_bucket(bucket_name, location="cn-north-1")
            # 判断图片是否存在
            isExist = self.isObjectExist(bucket_name, pdf_name)
            if isExist == "false":
                self.minioClient.put_object(bucket_name, pdf_name, pdf_data, pdf_size, content_type='application/pdf')
            # 拼接上传到公司服务器中的url路径
            pdf_utl = self.minioUrl + bucket_name + "/" + pdf_name
            return pdf_utl
        except InvalidResponseError as err:
            print(err)


if __name__ == '__main__':
    result = MinIOUtil()
    #     minioClient = Minio('192.168.1.191:9000',
    #                         access_key='admin',
    #                         secret_key='admin123456',
    #                         secure=False)
    #
    #     try:
    #         bucket_name = "images"
    #         img_name = "奔驰334w0.png"
    #         # 判断图片是否存在
    #         result = isObjectExist(bucket_name, img_name)
    #         print(result)
    #         # 上传pdf文档
    #         # print(minioClient.fput_object('images', '技术要求.pdf',
    #         #                               r'C:\Users\Administrator\Desktop\技术要求.pdf',
    #         #                               content_type='application/pdf'))
    #     except InvalidResponseError as err:
    #         print(err)
    # rr = result.get_image_name(
    #     "https://media.zenfs.com/en/video.tvbs.com.tw/2c487394091e6e1197314f6278070518")
    # print(rr)
    isExist = result.isObjectExist("2024vote", "video/003d7f2e-3bc8-3d7a-a488-5a7d5403baf4.mp4")
    print(isExist)
