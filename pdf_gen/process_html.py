"""
本来想用这个代码来把下载的原始的 html 处理一下， 得到简单的 html 只有网页新闻的 正文和图片
逻辑是
直接暴力遍历html的element , 一般情况下 就是名字叫做 img p a  figure 这样的名字
把他们存在数组里
再遍历数组 生成 新的html 这样就过滤了乱七八糟的 script 。。。
"""


import io
import os.path

import requests
from bs4 import BeautifulSoup

class ProHtml:
    def __init__(self):
        self.content_array = []
        self.string_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dynamic HTML</title>
</head>
<body>
"""

    def download_image(self, link, img_filename):
        r = requests.get(url=link, stream=True)
        # 获取到图片二进制流实现io.RawIOBase的python对象。
        img_data = io.BytesIO(r.content)
        path = os.path.join('res/', img_filename)
        # 将二进制数据写入本地文件
        with open(path, 'wb') as f:
            f.write(img_data.read())
        return path


    def process(self, html_content):
        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        for element in soup.descendants:

            if element.name == 'img' or element.name == 'a' or element.name == 'figure':
                print(element.name)
                # 处理图片
                img_link = element.get('src')

                if img_link is not None:
                    self.content_array.append(f'图片地址: {img_link}')
                else:
                    continue
            elif element.name == 'p' or element.name == 'font':
                print(element.name)
                # 处理段落文本
                text = element.get_text(strip=True)
                if text is not None:
                    self.content_array.append(f'段落文本: {text}')


        # 寻找第一个段落文本的位置
        first_paragraph_index = next((i for i, content in enumerate(self.content_array) if '段落文本' in content), None)

        # 寻找最后一个段落文本的位置
        last_paragraph_index = next((i for i, content in enumerate(reversed(self.content_array)) if '段落文本' in content), None)

        if first_paragraph_index is not None and last_paragraph_index is not None:
            # 删除在第一个段落文本之前的元素
            self.content_array = self.content_array[first_paragraph_index:]

            # 删除在最后一个段落文本之后的元素
            self.content_array = self.content_array[:-last_paragraph_index]

        self.pro_html()
        return self.string_html


    def pro_html(self):
        for i, content in enumerate(self.content_array):
            if "图片地址" in content:
                link = content.split(': ')[1]
                if link.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    # 如果链接是图片，下载图片并替换原来的链接为本地图片路径
                    img_filename = f'local_image_{i}.png'  # 保存的本地文件名
                    path = self.download_image(link, img_filename)
                    path = "file:///C:/Users/RZ/OneDrive/PycharmProjects/workspace/pdf_gen/" + path
                    self.content_array[i] = f'图片地址: {path}'
                    next_element = "<p><a><img src='{}'></a></p>".format(path)
                    self.string_html += "\n"
                    self.string_html += next_element
                else:
                    del self.content_array[i]
            elif "段落文本" in content:
                text = content.split(': ')[1]
                next_element = "<p style='font-size: 28px;'>{}</p>".format(text)
                self.string_html += "\n"
                self.string_html += next_element
        print(self.string_html)


    def get_content_array(self):
        return self.content_array
