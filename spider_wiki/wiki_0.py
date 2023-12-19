import pandas as pd
from selenium_tool.selenuim_tool import SeleniumTool
from selenium.common.exceptions import NoSuchElementException

# excel_path = r'C:\Users\RZ\OneDrive\桌面\2024立委信息爬虫.xlsx'
excel_path = r'C:\Users\RZ\OneDrive\桌面\立委专项数据\人物信息收集\立委数据爬虫\2024立委信息爬虫.xlsx'

excel_file = pd.ExcelFile(excel_path)
sheet_name = "spider4"
df = excel_file.parse(sheet_name)

# print(df['Name'])
url = "https://zh.wikipedia.org/zh-hans/"
selenium_tool = SeleniumTool()


list_inf = ['性别', '别名', '出生', '国籍', '配偶']

# df_info = pd.DataFrame(columns=['Name', '性别', '别名', '出生', '国籍', '配偶'])

for index, row in df.iterrows():
    name = row['Name']
    print(url + name)
    selenium_tool.open_web(url + name)
    tr_list = selenium_tool.driver.find_elements_by_xpath('//table[@class="infobox vcard"]/tbody/tr')
    for tr in tr_list:
        # print(tr.text)
        try:
            th = tr.find_element_by_xpath("./th")
            # print(th.text)
            if th.text in list_inf:
                td = tr.find_element_by_xpath('./td').text
                row[th.text] = td
                print(td)
        except NoSuchElementException:
            pass
    df.loc[index] = row
    print(row)

df.to_excel('立委数据_添加1.xlsx')
# df.to_excel('平地and山地_1.xlsx')








