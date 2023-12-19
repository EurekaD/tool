import os
import re
import time
import uuid

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def download_image(url, folder_path, name):
    file_extension = os.path.splitext(url)[1]
    name += file_extension
    response = requests.get(url)
    if response.status_code == 200:
        # 确保文件夹存在
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        # 构造文件路径
        file_path = os.path.join(folder_path, name)
        # 保存文件
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"文件已保存到 {file_path}")
        return file_path
    else:
        print(f"下载失败，HTTP状态码: {response.status_code}")


class SeleniumTool:
    def __init__(self):
        options = Options()
        chrome_path = "D:\selenium_chromedriver\chromedriver.exe"
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        )

        self.driver = webdriver.Chrome(executable_path=chrome_path ,options=options)
        self.wait = WebDriverWait(self.driver, 15)  # 设置最长等待时间为10秒

    def open_web(self, url):
        self.driver.get(url)
        time.sleep(3)

    def wait_element(self, xpath):
        # wait = WebDriverWait(self.driver, 2)
        self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    def wait_and_input(self, xpath, input_content):
        wait = WebDriverWait(self.driver, 2)
        wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

        # 定位输入框并输入文本
        input_box = self.driver.find_element(By.XPATH, xpath)
        input_box.send_keys(input_content)

    def wait_and_click(self, xpath):
        wait = WebDriverWait(self.driver, 2)
        wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        # 定位按钮并点击
        button = self.driver.find_element(By.XPATH, xpath)
        button.click()

    def spider_content(self, p_xpath):
        """
        p_xpath 段落的xpath
        """
        p_list = self.driver.find_elements_by_xpath(p_xpath)
        text = ''.join([p.text for p in p_list])
        print(text)
        return text





