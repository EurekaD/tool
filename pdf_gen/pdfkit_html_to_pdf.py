"""
这个可以把用 pdfkit 把 html 转成 pdf
但是它需要依赖一个 exe 【wkthmltopdf】 ,需要下载安装， linux版本也有 path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\
"""

import pdfkit
from selenium_get_html import GetHtml
from process_html import ProHtml


options = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': 'UTF-8',
    'no-outline': None,
    "enable-local-file-access": "",
}


def html_to_pdf(html, to_file):
    path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    pdfkit.from_string(html, to_file, configuration=config, options=options)


get_html = GetHtml()
pro_html = ProHtml()

# url = 'https://www.cmmedia.com.tw/home/articles/42987'
url = 'http://www.my-formosa.com/DOC_199361.htm'

html = get_html.get_html(url)

html_pro = pro_html.process(html)

html_to_pdf(html_pro, 'test1.pdf')