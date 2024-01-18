# -*- coding: utf-8 -*-
"""
@Time    : 2023/12/11 11:14
@Author  : kangaroo
@File    : data_count.py
@Software: PyCharm
@Dex     :
"""
# 导入pandas 和 pymysql 包
import pandas as pd
import pymysql
from sqlalchemy import create_engine, text
import time
from datetime import datetime

if __name__ == '__main__':
    con = pymysql.connect(
        host="192.168.1.162",
        port=3307,
        database="2024election",
        user="dataplatform",
        password="Dataplatform@2021"
    )
    # 创建mysql游标
    cursor = con.cursor()
    # update_time = time.strftime("%Y-%m-%d %H:%m:%S", time.localtime())
    update_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # print(update_time)
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    # 读取数据表中的数据
    # read_sql = "select * from `index_event2` where id =%s"
    index_insert = "replace into `data_count`(`id`,`yuqing_count`,`history_count`,`total_count`,`update_time`) values(%s,%s,%s,%s,%s)"

    houmepage_data_count = "insert into `homepage_data_count`(`total`,`seven_day_total`,`today_total`)values (%s,%s,%s)"

    engine_162_3307 = create_engine('mysql+pymysql://dyj:dyj123456@192.168.1.162:3307/2024election?charset=utf8')

    query_sql_162_3307 = "select sum(t.data_count)  as data_sum from (select count(1) as data_count FROM ads_jhy_popular_events union all " \
                         "select count(1) as data_count FROM  dp_ads.ads_jhy_popular_events  union all " \
                         "select count(1) as data_count FROM  xm_task.xm_hotspot_info  union all " \
                         "select count(1) as data_count FROM  xm_task.xm_hotspot_info_hot  union all " \
                         "select count(1) as data_count FROM  xm_task.search_keyword  union all " \
                         "select count(1) as data_count FROM dp_ads.ads_jhy_popular_events_copy1 ) as t "

    engine_189 = create_engine('mysql+pymysql://root:Dataplatform2023@192.168.1.189:3308/index_platform?charset=utf8')
    query_sql_189_3308 = "