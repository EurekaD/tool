import io
import os

import requests
from PIL import Image
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from selenium import webdriver

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
CHROME_DRIVER_PATH = r"chromedriver.exe"

script_dir = os.path.dirname(os.path.realpath(__file__))

# 保存文字和图片的数组
content_array = []

def download_image(link, img_filename):
    r = requests.get(url=link, stream=True)
    # 获取到图片二进制流实现io.RawIOBase的python对象。
    img_data = io.BytesIO(r.content)
    # 将二进制数据写入本地文件
    with open(img_filename, 'wb') as f:
        f.write(img_data.read())


def process_links():
    for i, content in enumerate(content_array):
        if "图片地址" in content:
            link = content.split(': ')[1]
            if link.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                # 如果链接是图片，下载图片并替换原来的链接为本地图片路径
                img_filename = f'local_image_{i}.png'  # 保存的本地文件名
                download_image(link, img_filename)
                content_array[i] = f'图片地址: {img_filename}'


def generate_pdf(output_pdf):
    # 创建PDF文件
    pdf = canvas.Canvas(output_pdf, pagesize=letter)

    # 设置字体和字号
    pdf.setFont("Helvetica", 12)

    process_links(content_array)

    # 写入内容到PDF
    for content in content_array:
        if "段落文本" in content:
            pdf.drawString(100, pdf._pagesize[1] - 100, content)  # 适当调整坐标
            pdf.translate(0, -15)  # 调整行间距
        elif "图片地址" in content:
            img_filename = content.split(': ')[1]
            img_path = os.path.join(script_dir, img_filename)
            img = Image.open(img_path)  # 打开图片
            print("正在插入图片：{}".format(img_path))
            pdf.drawInlineImage(img, 100, pdf._pagesize[1] - 200)  # 适当调整坐标

    # 保存PDF
    pdf.save()

def crawl_and_generate_pdf(url, output_pdf):
    # 指定webdriver的路径，替换为你本地的路径
    webdriver_path = CHROME_DRIVER_PATH

    # 创建Chrome浏览器实例
    driver = webdriver.Chrome(executable_path=webdriver_path)

    # 打开网页
    driver.get(url)

    # 获取网页的HTML内容
    html_content = driver.page_source

    # 关闭浏览器
    driver.quit()

    # 输出HTML内容
    print(html_content)
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # 遍历HTML
    for element in soup.descendants:
        if element.name == 'img' or element.name == 'a':
            # 处理图片
            img_link = element.get('href')
            if img_link is not None:
                content_array.append(f'图片地址: {img_link}')
            else:
                continue
        elif element.name == 'p':
            # 处理段落文本
            text = element.get_text(strip=True)
            content_array.append(f'段落文本: {text}')

    # 寻找第一个段落文本的位置
    first_paragraph_index = next((i for i, content in enumerate(content_array) if '段落文本' in content), None)

    # 寻找最后一个段落文本的位置
    last_paragraph_index = next((i for i, content in enumerate(reversed(content_array)) if '段落文本' in content), None)

    if first_paragraph_index is not None and last_paragraph_index is not None:
        # 删除在第一个段落文本之前的元素
        content_array = content_array[first_paragraph_index:]

        # 删除在最后一个段落文本之后的元素
        content_array = content_array[:-last_paragraph_index]

    # 打印保存的内容数组
    for content in content_array:
        print(content)

    generate_pdf(content_array, output_pdf)


if __name__ == '__main__':
    url = 'https://www.cmmedia.com.tw/home/articles/42987'
    output_pdf = '1.pdf'
    crawl_and_generate_pdf(url, output_pdf)
