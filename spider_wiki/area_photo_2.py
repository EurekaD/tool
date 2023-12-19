import pandas as pd
from selenium_tool.selenuim_tool import SeleniumTool
from selenium.common.exceptions import NoSuchElementException

df_area = pd.DataFrame(columns=['选举区', '现任议员'])
url = "https://zh.wikipedia.org/wiki/2024%E5%B9%B4%E4%B8%AD%E8%8F%AF%E6%B0%91%E5%9C%8B%E7%AB%8B%E6%B3%95%E5%A7%94%E5%93%A1%E9%81%B8%E8%88%89#%E9%81%B8%E8%88%89%E5%8D%80%E5%8A%83%E5%88%86%E8%88%87%E5%90%8D%E7%A8%B1%E8%AE%8A%E6%9B%B4"
selenium_tool = SeleniumTool()
selenium_tool.open_web(url)
td_list = selenium_tool.driver.find_elements_by_xpath("//table[@class='wikitable collapsible']/tbody/tr/td[1]/a")
list_area_name = []
list_href = []

for td in td_list:
    area_name = td.get_attribute('innerText')
    href = td.get_attribute('href')

    if '区' not in area_name:
        break

    list_area_name.append(area_name)
    list_href.append(href)

print(list_area_name)
print(list_href)

index = 0
name_1 = ''
for name, url in zip(list_area_name, list_href):
    selenium_tool.open_web(url)

    try:
        name_1 = selenium_tool.driver.find_element_by_xpath(
                "//table/tbody/tr/th[contains(text(),'现任议员')]/following-sibling::td/a[1]").get_attribute('title')
    except NoSuchElementException as e:
        print(e)
    finally:
        df_area.loc[index, '选举区'] = name
        df_area.loc[index, '现任议员'] = name_1
        print(name_1)
        name_1 = ''
        index += 1

df_area.to_excel('现任议员.xlsx')


