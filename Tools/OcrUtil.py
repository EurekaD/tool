'''
@File: OcrUtil.py
@Copyright: Guanchang3
@Date: 2022/10/26
@Desc: 利用easyocr获取图片中的文字
'''
import easyocr
from Tools.OpenccUtils import ctozhLite


def getcha(img):
    reader = easyocr.Reader(['ch_tra', 'en'])
    params = reader.readtext(img, detail=0)
    paragraph_list = []
    for i in params:
        i = ctozhLite(i)
        paragraph_list.append(i.replace(' ', '').replace('\n', ''))
    paragraph = ''.join(p for p in paragraph_list)
    return paragraph