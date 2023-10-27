"""
用 selenium 做自动化 的网站点击
但是问题在于 selenium 总是会自己打开一个新的 浏览器窗口 这个浏览器窗口 可能没有我的用户信息 感觉一些网站会出问题
网上查 可以使用 session_id 直接打开 我自己的浏览器窗口， （暂时没有成功，也可能是其他的问题）
"""

import re
import time
import uuid
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# session_id = '9292'
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("debuggerAddress", f"localhost:{session_id}")

options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=options)

wait = WebDriverWait(driver, 15)  # 设置最长等待时间为10秒


def open_web(url):
    driver.get(url)
    time.sleep(3)

url = 'http://www.my-formosa.com/DOC_199361.html'

open_web('https://www.printfriendly.com/')


def wait_and_input(xpath, input_content):
    wait = WebDriverWait(driver, 2)
    wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    # 定位输入框并输入文本
    input_box = driver.find_element(By.XPATH, xpath)
    input_box.send_keys(input_content)


def wait_and_click(xpath):
    wait = WebDriverWait(driver, 2)
    wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    # 定位按钮并点击
    button = driver.find_element(By.XPATH, xpath)
    button.click()


wait_and_click('/html/body/div/div[2]/div[1]/nav/div[2]/a[1]')

wait_and_input('//*[@id="Email"]', 'chenlin_091@163.com')
wait_and_input('//*[@id="Password"]', 'Chenlin6!')

wait_and_click('//*[@id="new_user"]/input[3]')


wait_and_click('//div/a/img')

wait_and_input("//input[@id='url']", url)
wait_and_click("//input[@class='button w-button']")

