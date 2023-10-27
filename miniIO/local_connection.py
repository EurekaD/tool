#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Guanchang3
# @Desc  : TODO 国盛驾驶舱-mysql连接信息
import pymysql
import time
from minio import Minio



class local_connection:
    def __init__(self):
        self.etl_create_time = time.strftime("%Y-%m-%d", time.localtime())
        self.etl_update_time = time.strftime("%Y-%m-%d", time.localtime())
        self.etl_create_date = time.strftime("%Y-%m-%d", time.localtime())
        self.etl_update_date = time.strftime("%Y-%m-%d", time.localtime())
        self.source_sys_id = '1'
        self.operater_id = '2'
        self.create_time = 'kangaroo'

        # minio 正式库 连接信息
        self.minioClient = Minio('192.168.1.182:9000',
                                 access_key='admin',
                                 secret_key='admin123456',
                                 secure=False)
        self.minioUrl = 'http://192.168.1.182:9000/'
        # minio 备份库 连接信息
        # self.minioClient = Minio('192.168.1.189:9091',
        #                          access_key='admin',
        #                          secret_key='admin123456',
        #                          secure=False)
        # self.minioUrl = 'http://192.168.1.189:9090/'

        # pymysql用连接信息
        # self.insert_connection = pymysql.connect(
        #     port=3307,
        #     host='192.168.1.162',
        #     user="dataplatform",
        #     password='Dataplatform@2021',
        #     db='dp_ads',
        #     cursorclass=pymysql.cursors.DictCursor,
        #     autocommit=True,
        #     charset='utf8'
        # )

        # pymysql测试库连接信息
        self.insert_connection = pymysql.connect(
            port=3308,
            host='192.168.1.189',
            user="root",
            password='Dataplatform2023',
            db='test1',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True,
            charset='utf8'
        )

        # pandasql用连接信息
        self.conn_info = 'mysql+pymysql://root:Ds$2020Ylg@192.168.1.162:3306/dp_ods?charset=utf8'
        self.insert_conn_info = 'mysql+pymysql://root:Ds$2020Ylg@192.168.1.162:3306/dp_ads?charset=utf8'
