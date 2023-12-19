#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : DataSource.py
# @Author: kangaroo
# @Date  : 2022/9/26 14:00
# @Desc  : 配置插入的数据源


import pymysql


class DataSource:
    def __init__(self):
        # mysql连接信息
        self.mysql_conn = pymysql.connect(
            host='192.168.1.162',
            port=3307,
            user='dataplatform',
            password='Dataplatform@2021',
            database='xm',
            charset='utf8')
        # pymysql189测试库连接信息
        self.insert_connection = pymysql.connect(
            port=3308,
            host='192.168.1.189',
            user="root",
            password='Dataplatform2023',
            database='public_opinion',
            charset='utf8mb4')

        self.vote_connection = pymysql.connect(
            host='192.168.1.162',
            port=3307,
            user='dataplatform',
            password='Dataplatform@2021',
            database='2024election',
            charset='utf8')