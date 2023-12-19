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

df_introduce = pd.DataFrame(columns=['Name', 'introduce'])

for index, row in df.iterrows():
    name = row['Name']
    print(url + name)
    selenium_tool.open_web(url + name)
    try:
        p1 = selenium_tool.driver.find_element_by_xpath('//div/p[1]')
        # row['人物介绍'] = p1.text
        print(p1.text)
        new_row = {'name': name, 'introduce': p1.text}
        df_introduce.loc[len(df_introduce)] = new_row
    except NoSuchElementException:
        pass

    # df.loc[index] = row
    # print(row)


# df.to_excel('立委数据_人物介绍.xlsx')
df_introduce.to_excel('添加_人物介绍.xlsx')