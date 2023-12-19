"""
用于爬取 wiki 上的人物信息
使用 selenium
【右侧 信息模块】，【正文， 可选择】
"""
import re

import pandas as pd
from selenium_tool.selenuim_tool import SeleniumTool
from selenium.common.exceptions import NoSuchElementException

class WikiSpider:
    def __init__(self, excel_path, sheet_name):
        self.name = None
        self.selenium_tool = SeleniumTool()
        self.url = "https://zh.wikipedia.org/zh-hans/"
        self.excel_path = r'C:\Users\RZ\OneDrive\桌面\2024立委信息爬虫.xlsx'
        self.excel_file = pd.ExcelFile(excel_path)
        self.sheet_name = sheet_name
        self.df = self.excel_file.parse(self.sheet_name)
        self.list_inf = ['性别', '别名', '出生', '国籍', '配偶']
        # 如需保存，定义
        # self.df_bad_news = pd.DataFrame(columns=['name', '事件名称', '时间', '内容'])

    def traversal_name(self):
        for index, row in self.df.iterrows():
            self.name = row['Name']
            print(self.url + self.name)
            self.selenium_tool.open_web(self.url + self.name)
            # 打开网站，进行所需信息获取

        self.save()

    def save(self, excel_name):
        # self.df_bad_news.to_excel(excel_name)
        pass



    def main_content(self):
        # 中央大段内容， 下面是示例，争议标题下的正文
        p_list = self.selenium_tool.driver.find_elements_by_xpath("//*[contains(text(), '争议')]/..//following-sibling::p")
        for p in p_list:
            text = p.text
            print(self.extract_dates(text))
            new_row = {'name': self.name, '时间': self.extract_dates(text), '内容': text}
            # 如需保存，在此使用
            # df_bad_news.loc[len(df_bad_news)] = new_row


    def side_info_box(self):
        # 右侧信息框
        pass


    def extract_dates(self, text):
        year_pattern = re.compile(r'(\d{4})年')
        month_pattern = re.compile(r'(\d{1,2})月')
        day_pattern = re.compile(r'(\d{1,2})日')
        years = re.findall(year_pattern, text)
        months = re.findall(month_pattern, text)
        days = re.findall(day_pattern, text)
        # 构建日期格式
        formatted_date = ""
        # 添加年份部分
        if years:
            formatted_date += f"{years[0]}"
        # 添加月份部分
        if months:
            formatted_date += f"-{months[0]}"
        # 添加日期部分
        if days:
            formatted_date += f"-{days[0]}"
        return formatted_date

