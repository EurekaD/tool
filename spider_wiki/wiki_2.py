import pandas as pd
from selenium_tool.selenuim_tool import SeleniumTool
from selenium.common.exceptions import NoSuchElementException
# excel_path = r'C:\Users\RZ\OneDrive\桌面\2024立委信息爬虫.xlsx'
excel_path = r'C:\Users\RZ\OneDrive\桌面\立委专项数据\人物信息收集\立委数据爬虫\2024立委信息爬虫.xlsx'
excel_file = pd.ExcelFile(excel_path)
sheet_name = "spider4"
df = excel_file.parse(sheet_name)

df_edu = pd.DataFrame(columns=['name', 'edu'])
df_exp = pd.DataFrame(columns=['name', 'exp'])

# print(df['Name'])
url = "https://zh.wikipedia.org/zh-hans/"
selenium_tool = SeleniumTool()


for index, row in df.iterrows():
    name = row['Name']
    print(url + name)
    selenium_tool.open_web(url + name)
    tr_list = selenium_tool.driver.find_elements_by_xpath('//table[@class="infobox vcard"]/tbody/tr')
    for tr in tr_list:
        try:
            element = tr.find_element_by_xpath("./td/div/div")
            # print(element.text)
            if element.text == '经历':
                exp_list = tr.find_elements_by_xpath('./td/div/ul/li/ul/ul/li')
                for exp in exp_list:
                    # print('经历')
                    # a = exp.find_element_by_xpath("./a")
                    exp_text = selenium_tool.driver.execute_script("return arguments[0].innerText;", exp)
                    print(exp_text)
                    # print(exp.get_attribute('outerHTML'))
                    # print(exp.get_attribute('innerHTML'))
                    new_row = {'name': name, 'exp': exp_text}
                    df_exp.loc[len(df_exp)] = new_row

            elif element.text == '学历':
                edu_list = tr.find_elements_by_xpath('./td/div/ul/li/ul/ul/li')
                for edu in edu_list:
                    edu_text = selenium_tool.driver.execute_script("return arguments[0].innerText;", edu)
                    print(edu_text)
                    new_row = {'name': name, 'edu': edu_text}
                    df_edu.loc[len(df_edu)] = new_row
            else:
                print('这个 tr 不是')
        except NoSuchElementException:
            pass

df_exp.to_excel('立委数据_经历.xlsx')
df_edu.to_excel('立委数据_学历.xlsx')
# df_exp.to_excel('平地and山地_经历.xlsx')
# df_edu.to_excel('平地and山地_学历.xlsx')





