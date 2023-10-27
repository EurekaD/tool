"""
使用 printfriendly 的接口 传一个url，会返回给一个 路径 直接访问下载就行，不会直接返回文件 第二天这个路径就用不了了
但是 他会自动 加上水印 没办法用 或许可以写个能把水印自动去除的
一个账号只能 200次 调用
这是 key     c2f5061bfa4313f0c136c465cf941f3b
"""


import requests

def make_api_request(url, params=None, headers=None):
    try:
        response = requests.post(url, params=params, headers=headers)

        # 检查请求是否成功 (状态码为200)
        if response.status_code == 200:
            # 返回响应的JSON数据或其他内容
            print(response.json())  # 如果返回的是JSON数据
            # return response.text  # 如果返回的是文本数据
        else:
            print(f"请求失败，状态码: {response.status_code,response.json()}")
    except Exception as e:
        print(f"请求发生异常: {e}")

# 示例用法
api_url = "https://api.printfriendly.com/v2/pdf/create?api_key=c2f5061bfa4313f0c136c465cf941f3b"
# response_data = make_api_request(api_url)

# 如果有参数或需要设置headers，可以像这样传递：
params = {"page_url": "https://newtalk.tw/news/view/2023-10-02/890600"}
headers = {}
response_data = make_api_request(api_url, params=params, headers=headers)

