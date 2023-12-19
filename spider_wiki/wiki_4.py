import re

import pandas as pd
from selenium_tool.selenuim_tool import SeleniumTool
from selenium.common.exceptions import NoSuchElementException, TimeoutException

excel_path = r'C:\Users\RZ\OneDrive\桌面\2024立委信息爬虫.xlsx'

excel_file = pd.ExcelFile(excel_path)
sheet_name = "spider3"
df = excel_file.parse(sheet_name)

# print(df['Name'])
url = "https://zh.wikipedia.org/zh-hans/"
selenium_tool = SeleniumTool()

def extract_dates(text):
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


df_bad_news = pd.DataFrame(columns=['name', '事件名称', '时间', '内容'])


"""
<h2> 争议
<h3> 事件1 名称 
<p> 事件1 第一段
<p>
<p>
<h3> 事件2 名称 
<p>
<p>
following-sibling  用来选取同级的紧接着的元素 (用这个就不用 ..[..用来选取父级元素])
先选中 h2 ,再选 h2 后面的 两个 h3 ,再选中 h3 后面的 p_list
"""

# for index, row in df.iterrows():
#     name = row['Name']
#     print(url + name)
#     selenium_tool.open_web(url + name)
#
#     p_list = selenium_tool.driver.find_elements_by_xpath("//*[contains(text(), '争议')]/..//following-sibling::p")

#     for p in p_list:
#         text = p.text
#         print(name)
#         print(text)
#         print(extract_dates(text))
#         new_row = {'name': name, '时间': extract_dates(text), '内容': text}
#         df_bad_news.loc[len(df_bad_news)] = new_row

for index, row in df.iterrows():
    name = row['Name']
    print(url + name)
    selenium_tool.open_web(url + name)

    h_list = selenium_tool.driver.find_elements_by_xpath("//*[contains(text(), '争议')]/following-sibling::h3 | //*[contains(text(), '争议')]/following-sibling::h4")
    for h in h_list:
        h_text = h.find_element_by_xpath("/span").text
        p_list = h.find_elements_by_xpath("/following-sibling::p")
        for p in p_list:
            pass



# df_bad_news.to_excel('立委数据_争议.xlsx')
df_bad_news.to_excel('平地and山地_争议.xlsx')






