#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/25 19:35
# @Author  : Guanchang3
# @File    : generateWordCloud

import os
from collections import Counter
from datetime import datetime
# Setting up parallel processes :4 ,but unable to run on Windows
from os import path

# import jieba
# from imageio import imread
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image
from dateutil.relativedelta import relativedelta
# jieba.load_userdict("txt\userdict.txt")
# add userdict by load_userdict()
# from wordcloud import WordCloud, ImageColorGenerator
# from src.tools.OpenccUtils import ctozhLite
# from src.tools.DbUtils import DbUtils

project_path = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0] + '/../..'
# 上个月
last_month = datetime.strftime(datetime.now() - relativedelta(months=1), "%Y-%m-%d")
# 上个月无具体日期
l_month = datetime.strftime(datetime.now() - relativedelta(months=1), "%Y-%m")
# 当月
this_month = datetime.strftime(datetime.now(), "%Y-%m")


def Gener(query_keyword: str):
    # jieba.enable_parallel(4)
    # get data directory (using getcwd() is needed to support running example in generated IPython notebook)
    stopwords_path = project_path + '/src/stopwords/cn_stopwords.txt'
    # Chinese fonts must be set
    font_path = project_path + '/resource/fonts/SourceHanSerif/SourceHanSerifK-Light.otf'
    # Read the whole text.
    mysql_db = DbUtils("public_opinion")
    conn = mysql_db.get_conn()
    etl_update_date = datetime.now().strftime("%Y-%m-%d")
    # sql = f"""SELECT paragraph from monitor_news_event where operater_id = '{query_keyword}'"""
    sql = f"""SELECT
                    etl_id,
                    etl_create_time,
                    etl_update_date,
                    title,
                    abstract,
                    link_detail_href,
                    pub_time,
                    img_url,
                    searchword,
                    `source`,
                    paragraph
                FROM
                    monitor_news
                WHERE
                   pub_time>='2024-01-07' and paragraph like '%柯文哲%'"""
    # 修改成直接使用查询好的关键词进行生成关键词词云图
    # sql = f"""SELECT
    #                 paragraph
    #             FROM
    #                 monitor_news
    #             WHERE
    #                 etl_id IN (SELECT news_id FROM monitor_word_cloud where menu_name = '{query_keyword}')
    #                 """
    text = pd.read_sql_query(sql=sql, con=conn).to_string()
    conn.close()
    del mysql_db
    # the path to save worldcloud
    # imagename1 = this_month + '.png'
    imagename1 = this_month + query_keyword + ".png"

    # read the mask / color image taken from
    #     back_coloring = imread(path.join(d, d + '/wc_cn/kewenzhe_color.png'))

    # The function for processing text with Jieba
    # def jieba_processing_txt(text):
    #     mywordlist = []
    #     seg_list = jieba.lcut(text)
    #     liststr = "/ ".join(seg_list)
    #
    #     with open(stopwords_path, encoding='utf-8') as f_stop:
    #         f_stop_text = f_stop.read()
    #         f_stop_seg_list = f_stop_text.splitlines()
    #
    #     for myword in liststr.split('/'):
    #         if not (myword.strip() in f_stop_seg_list) and len(myword.strip()) > 1:
    #             mywordlist.append(myword)
    #     return ' '.join(mywordlist)
    # 文本处理函数，返回分词后的词列表
    # def jieba_processing_txt(text):
    #     mywordlist = jieba.lcut(text)
    #
    #     with open(stopwords_path, encoding='utf-8') as f_stop:
    #         f_stop_text = f_stop.read()
    #         f_stop_seg_list = f_stop_text.splitlines()
    #
    #     mywordlist = [word for word in mywordlist if word.strip() not in f_stop_seg_list and len(word.strip()) > 1]
    #     return mywordlist

    # 对文本进行分词处理，获取词列表
    # word_list = jieba_processing_txt(text)

    # 统计词频
    word_freq = Counter(word_list)
    print(type(word_freq))
    print(word_freq)

    # 设置"喂药"的权重
    word_freq["..."] = 1
    word_freq["00"] = 1
    word_freq["01"] = 1
    #word_freq["桃色"] = 1418
    #word_freq["台湾"] = 500
    # word_freq["立委"] = 1
    # word_freq["总统"] = 1
    # word_freq["台湾"] = 1
    # word_freq["政治"] = 1
    # word_freq["赖清德"] = 486
    # word_freq["国家"] = 1
    # word_freq["政治"] = 1
    # word_freq["参选人"] = 532
    # word_freq["政府"] = 1
    # word_freq["超思"] = 450
    # word_freq["蛋荒"] = 567
    # word_freq["陈吉仲"] = 438
    # word_freq["农业部"] = 585
    word_freq["柯文"] = 1
    word_freq["柯文哲"] = 2531

    wc = WordCloud(font_path=font_path,
                   background_color='rgba(255, 255, 255, 0)',
                   mode="RGBA",
                   colormap='PuBu',
                   #max_words=200,
                   max_words=150,
                   scale=2,
                   max_font_size=60,
                   min_font_size=4,
                   random_state=42,
                   #                    width=1000,
                   #                    height=860,
                   margin=2)

    wc.generate_from_frequencies(word_freq)

    # create coloring from image
    # image_colors_default = ImageColorGenerator(back_coloring)

    plt.figure()
    # recolor wordcloud and show
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()

    # save wordcloud
    wc.to_file(path.join(project_path + "/resource/images", imagename1))

    # create coloring from image
    # image_colors_byImg = ImageColorGenerator(back_coloring)

    # show
    # we could also give color_func=image_colors directly in the constructor
    # plt.imshow(wc.recolor(color_func=image_colors_byImg), interpolation="bilinear")
    # plt.axis("off")
    # plt.figure()
    # plt.imshow(back_coloring, interpolation="bilinear")
    # plt.axis("off")
    # plt.show()

    # save_svg
    #     wordcloud_svg = wc.to_svg(embed_font=True)
    #     f = open("luxun1.svg","w+")
    #     f.write(wordcloud_svg)
    #     f.close()
    # save wordcloud
    # wc.to_file(path.join(d, imgname2))


if __name__ == '__main__':
    #query_keyword = '赖清德'
    #query_keyword = '侯友宜'
    query_keyword = '柯文哲'
    Gener(query_keyword)
