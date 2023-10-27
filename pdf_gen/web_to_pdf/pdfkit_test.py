import pdfkit
import requests
import io
import os
from PIL import Image
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from selenium import webdriver
import pdfkit


options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'no-outline': None,
    "enable-local-file-access": ""
}


'''将网页url生成pdf文件'''
def html_to_pdf(html, to_file):
    # 将wkhtmltopdf.exe程序绝对路径传入config对象
    path_wkthmltopdf = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    # 生成pdf文件，to_file为文件路径
    pdfkit.from_string(html, to_file, configuration=config, options=options)
    print('完成')

html = """
<p>我的沙卡就是卡夫卡还是按时鉴定会卡士打双打和但是</p>
<p>爱啥啥大师大事的阿什顿萨达 是客户的哈桑上帝更多v公司的广东省VS的VS看的话v开始阶段和v肯定是v客户端</p>
<p>sssss</p>
<p><a><img src='file:///C:/Users/RZ/OneDrive/PycharmProjects/workspace/web_to_pdf/local_image_2.png'></a></p>
"""
html_to_pdf(html, 'test.pdf')
