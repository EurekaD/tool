import requests
import io
import os
from PIL import Image
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from selenium import webdriver
import pdfkit

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

    def generate_pdf(self, html, output_pdf):
        # 将wkhtmltopdf.exe程序绝对路径传入config对象
        path_wkthmltopdf = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        # 生成pdf文件，to_file为文件路径
        # pdfkit.from_url(url, output_pdf, configuration=config)
        pdfkit.from_string(html, output_path=output_pdf, configuration=config)
        print('完成')

    def crawl_and_generate_pdf(self, url, output_pdf):
        # 指定webdriver的路径，替换为你本地的路径
        webdriver_path = self.CHROME_DRIVER_PATH

        # 创建Chrome浏览器实例
        driver = webdriver.Chrome()

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
        for element in soup(True):  # soup(True) will return all tags in the soup
            if element.name not in ['img', 'p']:
                # 如果元素不是图片或段落，删除它
                element.extract()
            elif element.name == 'img' and not element.get('src'):
                # 如果元素是图片，但没有src属性，删除它
                element.extract()
            elif element.name == 'p' and not element.get_text(strip=True):
                # 如果元素是段落，但没有文本，删除它
                element.extract()

        # 将修改后的HTML转换为字符串
        HTML = str(soup)
        print(HTML)

        # self.generate_pdf(HTML, 'out_2.pdf')



if __name__ == '__main__':
    url = 'https://www.cmmedia.com.tw/home/articles/42987'
    # url = 'https://www.mnews.tw/story/20231018nm021'
    output_pdf = '1.pdf'
    test = WebPdf()

    test.crawl_and_generate_pdf(url, output_pdf)
