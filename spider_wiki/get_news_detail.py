import uuid

import pandas as pd
from selenium_tool.selenuim_tool import download_image,SeleniumTool


selenium_tool = SeleniumTool()
df = pd.read_excel(r'大事记录.xlsx')

text_list = []

for index, row in df.iterrows():
    url = row['href']
    selenium_tool.open_web(url)
    text = selenium_tool.spider_content('//div[@class="caas-body"]')
    text_list.append(text)

df['text'] = text_list

df.to_excel('大事记录_v2.xlsx')


# path = r'C:\Users\RZ\Pictures\big_thing2'
#
# for index, row in df.iterrows():
#     url = row['photo']
#     name = str(uuid.uuid1())
#     file_path = download_image(url, path, name)
#     row['photo'] = file_path
#     df.loc[index] = row
#
# df.to_excel('大事记录_v3.xlsx')
