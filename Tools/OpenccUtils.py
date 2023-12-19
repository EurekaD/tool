'''
@File: OpenccUtils.py
@Copyright: Guanchang3
@Date: 2022/8/12
@Desc: 繁简互转utils
'''

from opencc import OpenCC
from zhconv import convert
import re


def ctozh(str):
    # t2s 繁体到简体
    cc = OpenCC('t2s')
    res = cc.convert(str)
    return res


def ctosw(str):
    # s2t 简体到繁体
    cc = OpenCC('s2t')
    res = cc.convert(str)
    return res


def ctozhLite(str):
    # zh-cn 繁体转简体
    res = convert(str, 'zh-cn')
    return res

def ctoswLite(str):
    # zh-tw 简体转繁体
    res = convert(str, 'zh-tw')
    return res

def filter_emoji(desstr, restr=''):
    # 过滤表情
    try:
        co = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    return co.sub(restr, desstr)
