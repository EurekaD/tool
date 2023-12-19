
"""
用于将图片批量下载到本地，要先获取url，从excel里读取图片的地址
"""

import os.path
import random
from urllib.parse import unquote
import pandas as pd
import requests
import time

# 存有图片url 的excel
df = pd.read_excel(r'选取地图_2.xlsx')

# 下载到本地储存的位置
path = r"C:/Users/RZ/Pictures/立法委选举区域地图/2012_small/"

# 定义一个最大重试次数
max_retries = 3

# 定义一个延迟时间
delay = 1


# 定义一个proxy类
def get_proxy():
    proxy = '127.0.0.1:7890'
    proxies = {
        'http': 'http://' + proxy,
        'https': 'http://' + proxy
    }

    return proxies

headers = {"refer": "https://zh.wikipedia.org/",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}

# 遍历df的每一行
for index, row in df.iterrows():
    # 获取图片的URL，替换220px为1440px
    url = row['2012_small']
    print(index)
    # 如果URL不为空，type(url) is str【excel中如果是空的，读取后判断类型是float,而不是None】
    if type(url) is str:
        # 替换url中的清晰度，注意是否能够替换
        url = url.replace("220px", "1440px")
        print(url)
        # 初始化一个重试次数
        retries = 0
        # 使用一个循环，直到成功或达到最大重试次数
        while True:
            try:
                delay = random.randint(1, 10)
                # 让程序暂停delay秒
                time.sleep(delay)

                proxies = get_proxy()
                # 发送GET请求到URL，获取响应
                r = requests.get(url, proxies=proxies, headers=headers)
                # 如果响应状态码是200，表示成功
                if r.status_code == 200:
                    # 定义文件名，包含选举区， 配置下载后保存图片的名字
                    file_name = row['选举区'] + '.png'
                    # 拼接路径和文件名
                    file_name = path + file_name
                    # 打开文件，写入响应内容
                    with open(file_name, 'wb') as f:
                        f.write(r.content)
                    # 跳出循环
                    break
                # 如果响应状态码不是200，表示失败
                else:
                    # 抛出一个异常
                    raise Exception(f"请求失败，状态码为{r.status_code}")
            # 捕获异常
            except Exception as e:
                # 打印异常信息
                print(e)
                # 增加重试次数
                retries += 1
                # 如果重试次数小于最大重试次数
                if retries < max_retries:
                    # 打印重试信息
                    print(f"正在重试，第{retries}次")
                    # 等待一段时间
                    time.sleep(delay)
                # 如果重试次数达到最大重试次数
                else:
                    # 打印放弃信息
                    print(f"放弃下载，超过最大重试次数{max_retries}")
                    # 跳出循环
                    break
