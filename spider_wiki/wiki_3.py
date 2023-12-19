import pandas as pd
from selenium_tool.selenuim_tool import SeleniumTool
from selenium.common.exceptions import NoSuchElementException, TimeoutException

excel_path = r'C:\Users\RZ\OneDrive\桌面\立委专项数据\人物信息收集\立委数据爬虫\2024立委信息爬虫.xlsx'

excel_file = pd.ExcelFile(excel_path)
sheet_name = "spider4"
df = excel_file.parse(sheet_name)

df_photo = pd.DataFrame(columns=['name', 'photo'])


# print(df['Name'])
url = "https://zh.wikipedia.org/zh-hans/"
selenium_tool = SeleniumTool()


for index, row in df.iterrows():
    name = row['Name']
    print(url + name)
    selenium_tool.open_web(url + name)
    # tr_list = selenium_tool.driver.find_elements_by_xpath('//table[@class="infobox vcard"]/tbody/tr[2]')

    try:
        selenium_tool.wait_and_click('//table[@class="infobox vcard"]/tbody/tr[2]')
        selenium_tool.wait_and_click('/html/body/div[6]/div/div[1]/a[1]')
        selenium_tool.wait_and_click('/html/body/div[6]/div/div[2]/div/div[3]/div[3]/div[1]/a[1]/span[1]')
        new_row = {'name': name, 'photo': '1'}
        df_photo.loc[len(df_photo)] = new_row

        # 继续执行其他操作
    except TimeoutException:
        new_row = {'name': name, 'photo': '0'}
        df_photo.loc[len(df_photo)] = new_row
        print(f"Timeout for element with this XPath. Skipping to the next iteration.")
        continue

df_photo.to_excel('立委数据_照片.xlsx')
