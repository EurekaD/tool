import requests
import io
import os
from PIL import Image
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from selenium import webdriver

class WebPdf:
    def __init__(self):
        self.CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        self.CHROME_DRIVER_PATH = r"chromedriver.exe"
        self.script_dir = os.path.dirname(os.path.realpath(__file__))

        # 保存文字和图片的数组
        self.content_array = []

    def download_image(self, link, img_filename):
        r = requests.get(url=link, stream=True)
        # 获取到图片二进制流实现io.RawIOBase的python对象。
        img_data = io.BytesIO(r.content)
        # 将二进制数据写入本地文件
        with open(img_filename, 'wb') as f:
            f.write(img_data.read())

    def process_links(self):
        for i, content in enumerate(self.content_array):
            if "图片地址" in content:
                link = content.split(': ')[1]
                if link.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    # 如果链接是图片，下载图片并替换原来的链接为本地图片路径
                    img_filename = f'local_image_{i}.png'  # 保存的本地文件名
                    self.download_image(link, img_filename)
                    self.content_array[i] = f'图片地址: {img_filename}'
                else:
                    del self.content_array[i]

    def generate_pdf(self, output_pdf):
        # 创建PDF文件
        pdf = canvas.Canvas(output_pdf, pagesize=letter)

        # 设置字体和字号
        pdf.setFont("SimSun", 12)

        # 初始垂直位置
        y_position = pdf._pagesize[1] - 100

        self.process_links()

        # 写入内容到PDF
        for content in self.content_array:
            if "段落文本" in content:
                pdf.drawString(100, y_position, content)  # 适当调整坐标
            elif "图片地址" in content:
                img_path = content.split(': ')[1]
                img = Image.open(img_path)  # 打开本地图片
                img_width, img_height = img.size
                pdf.drawInlineImage(img, 100, y_position - img_height, width=img_width, height=img_height)  # 适当调整坐标
                y_position -= img_height + 15  # 调整行间距

        # 保存PDF
        pdf.save()

    def crawl_and_generate_pdf(self, url, output_pdf):
        # 指定webdriver的路径，替换为你本地的路径
        webdriver_path = self.CHROME_DRIVER_PATH

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
                    self.content_array.append(f'图片地址: {img_link}')
                else:
                    continue
            elif element.name == 'p':
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

        # 打印保存的内容数组
        for content in self.content_array:
            print(content)

        self.generate_pdf(output_pdf)

if __name__ == '__main__':
    url = 'https://www.cmmedia.com.tw/home/articles/42987'
    # url = 'https://www.mnews.tw/story/20231018nm021'
    output_pdf = '1.pdf'
    test = WebPdf()

    test.crawl_and_generate_pdf(url, output_pdf)
