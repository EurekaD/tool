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
    engine_1893 = create_engine('mysql+pymysql://root:Dataplatform2023@192.168.1.189:3308/public_opinion?charset=utf8')
    query_sql_189_3308 = "select sum(t.data_count) as data_sum  from (" \
                         "select count(1) as data_count FROM chdtv union all " \
                         "select count(1) as data_count FROM  guancha_news  union all " \
                         "select count(1) as data_count FROM ltncom union all " \
                         " select count(1)as data_count FROM  chdtv_realtime union all " \
                         " select count(1)as data_count FROM  ltncom_realtime union all " \
                         " select count(1)as data_count FROM  udncom union all " \
                         "select count(1)as data_count FROM  udncom_realtime union all " \
                         " select count(1)as data_count FROM wang_news union all " \
                         "select count(1)as data_count FROM   wang_news1 union all " \
                         "select count(1)as data_count FROM   wang_news2 union all " \
                         "select count(1)as data_count FROM   wang_news3 union all " \
                         "select count(1)as data_count FROM  wang_news4 union all " \
                         "select count(1)as data_count FROM  wang_news5 union all " \
                         "select count(1)as data_count FROM  wang_news6 union all " \
                         "select count(1)as data_count FROM  wang_news7 union all " \
                         "select count(1)as data_count FROM  wang_news8 union all " \
                         "select count(1)as data_count FROM  wang_news9 union all " \
                         " select count(1)as data_count FROM  sentiment_platform.twitter_comment union all " \
                         " select count(1)as data_count FROM  sentiment_platform.twitter_news union all " \
                         " select count(1)as data_count FROM  sentiment_platform.twitter_user union all " \
                         " select count(1)as data_count FROM  public_opinion.cna_news union all " \
                         " select count(1)as data_count FROM  public_opinion.yahoo_news_king union all " \
                         " select count(1)as data_count FROM  public_opinion.yahoo_news_yahoo union all " \
                         " select count(1)as data_count FROM  public_opinion.yahoo_news_twsb union all " \
                         " select count(1)as data_count FROM  public_opinion.hongkong01_news union all " \
                         " select count(1)as data_count FROM  public_opinion.monitor_videos ) as t "

    count_7day_data = "SELECT COUNT(1) AS data_count FROM public_opinion.monitor_news AS mn WHERE DATE(mn.etl_create_time) >= CURDATE() - INTERVAL 7 DAY"
    count_24Hours_data = "SELECT COUNT(1) AS data_count FROM public_opinion.monitor_news AS mn WHERE mn.etl_create_time >= NOW() - INTERVAL 24 HOUR"

    # 189服务器上mysql舆情平台数据量统计
    query_189 = pd.read_sql_query(text(query_sql_189_3308), con=engine_189.connect())

    # 189服务器上mysql舆情平台的7天数据量
    datacount_7day = pd.read_sql_query(text(count_7day_data), con=engine_189.connect())
    # 189服务器上24小时的数据量统计
    datacount_24hour = pd.read_sql_query(text(count_24Hours_data), con=engine_189.connect())

    # 162服务器上mysql舆情平台数据量统计
    query_162 = pd.read_sql_query(text(query_sql_162_3307), con=engine_162_3307.connect())

    # pd.set_option('display.unicode.ambiguous_as_wide', True)
    # pd.set_option('display.unicode.east_asian_width', True)
    query_189['data_sum'] = query_189['data_sum'].astype('int')

    query_162['data_sum'] = query_162['data_sum'].astype('int')
    yuqing_count = query_189['data_sum'][0] + query_162['data_sum'][0]
    print(yuqing_count)
    history_count = 11712542
    print("zongshu", str(yuqing_count + history_count))
    id = 1
    # cursor.execute(index_insert, (id,yuqing_count, history_count, yuqing_count + history_count, update_time))
    # data = {"value": [yuqing_count, datacount_7day['data_count'][0], datacount_24hour['data_count'][0]], }#total`,``,`today_total
    data = {"total": yuqing_count,
            "seven_day_total": datacount_7day['data_count'][0], "today_total": datacount_24hour['data_count'][0]}
    data3 = [yuqing_count, datacount_7day['data_count'][0],datacount_24hour['data_count'][0]]
    print(data)
    shouye = pd.DataFrame({'total': yuqing_count, "seven_day_total": datacount_7day['data_count'][0], "today_total": datacount_24hour['data_count'][0]},index=[0])
    shouye.to_sql(name="homepage_data_count", con=engine_1893, if_exists='append',index=False)
    engine_1893.dispose()
    engine_189.dispose()
    engine_162_3307.dispose()
    print(shouye)
    print("poidjfpaoisjfpoqiw")
    con.commit()
    cursor.close()
    con.close()
