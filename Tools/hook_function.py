#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    @author: yongjie.dai
    @contact:dyj@softline.sh.cn
    @version: 1.0.0
    @license: Apache Licence
    @file: hook_function.py
    @time: 2023/11/1 13:45
    @software: PyCharm 
    @Des: 工具函数方法
"""

from datetime import datetime


def strDate_to_date(date_string, date_format):
    """
    :return: 返回日期格式为00000000
    :param date_string: 字符串时间："2023/10/9 10:44"
    :type date_format: 时间格式如："%Y/%m/%d %H:%M"
    """
    date_object = datetime.strptime(date_string, date_format).date()
    formatted_date = date_object.strftime("%Y%m%d")

    return formatted_date
