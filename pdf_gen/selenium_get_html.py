"""
使用 selenium 得到一个 url 的 html
"""

from selenium import webdriver

class GetHtml:
    def __init__(self):
        self.CHROME_DRIVER_PATH = r"chromedriver.exe"

    def get_html(self, url):
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

        return html_content
