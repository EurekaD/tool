import pandas as pd
from selenium_tool.selenuim_tool import SeleniumTool
from selenium.common.exceptions import NoSuchElementException

df_area = pd.DataFrame(columns=['选举区', '选区占地', '选取介绍', 'big_area', '2020_small', '2016_small', '2012_small'])
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
p1 = ""
p2 = ""
p3 = ""
big_area = ""
small_2020 = ""
small_2016 = ""
small_2012 = ""

for name, url in zip(list_area_name, list_href):
    selenium_tool.open_web(url)
    df_area.loc[index, '选举区'] = name
    # try:
    #     p1 = selenium_tool.driver.find_element_by_xpath(
    #         "//div[@class='mw-content-ltr mw-parser-output']/p[1]").get_attribute('innerText')
    #     p2 = selenium_tool.driver.find_element_by_xpath(
    #         "//div[@class='mw-content-ltr mw-parser-output']/p[2]").get_attribute('innerText')
    #     p3 = selenium_tool.driver.find_element_by_xpath(
    #         "//div[@class='mw-content-ltr mw-parser-output']/p[3]").get_attribute('innerText')
    # except NoSuchElementException as e:
    #     print(e)
    # finally:
    #     df_area.loc[index, '选区占地'] = p3
    #     df_area.loc[index, '选取介绍'] = p1 + p2
    #
    #     p1 = ""
    #     p2 = ""
    #     p3 = ""
    # try:
    #     selenium_tool.wait_and_click("//*[@id='mw-content-text']/div[1]/table[1]/tbody/tr[4]/td/span/a/img")
    #     big_area = selenium_tool.driver.find_element_by_xpath(
    #         "//div[@class='mw-mmv-image']/img"
    #     ).get_attribute('src')
    #     print(big_area)
    #     df_area.loc[index, 'big_area'] = big_area
    # except NoSuchElementException as e:
    #     print(e)
    # finally:
    #     selenium_tool.wait_and_click("//*[@class='mw-mmv-close']")
    #
    # try:
    #     selenium_tool.wait_and_click("//figcaption[contains(text(), '2020')]/preceding-sibling::a/img")
    #     small_2020 = selenium_tool.driver.find_element_by_xpath(
    #         "//div[@class='mw-mmv-image']/img"
    #     ).get_attribute('src')
    #     print(small_2020)
    #     df_area.loc[index, '2020_small'] = small_2020
    # except NoSuchElementException as e:
    #     print(e)
    # finally:
    #     selenium_tool.wait_and_click("//*[@class='mw-mmv-close']")
    #
    # try:
    #     selenium_tool.wait_and_click("//figcaption[contains(text(), '2016')]/preceding-sibling::a/img")
    #     small_2016 = selenium_tool.driver.find_element_by_xpath(
    #         "//div[@class='mw-mmv-image']/img"
    #     ).get_attribute('src')
    #     print(small_2016)
    #     df_area.loc[index, '2016_small'] = small_2016
    #     selenium_tool.wait_and_click("//*[@class='mw-mmv-close']")
    # except NoSuchElementException as e:
    #     print(e)
    # finally:
    #     selenium_tool.wait_and_click("//*[@class='mw-mmv-close']")
    #
    # try:
    #     selenium_tool.wait_and_click("//figcaption[contains(text(), '2012')]/preceding-sibling::a/img")
    #     small_2012 = selenium_tool.driver.find_element_by_xpath(
    #         "//div[@class='mw-mmv-image']/img"
    #     ).get_attribute('src')
    #     print(small_2012)
    #     df_area.loc[index, '2012_small'] = small_2012
    # except NoSuchElementException as e:
    #     print(e)
    # finally:
    #     selenium_tool.wait_and_click("//*[@class='mw-mmv-close']")

    try:
        big_area = selenium_tool.driver.find_element_by_xpath(
            "//tbody/tr/td/span/a/img"
        ).get_attribute('src')

        small_2020 = selenium_tool.driver.find_element_by_xpath(
            "//figcaption[contains(text(), '2020')]/preceding-sibling::a/img"
        ).get_attribute('src')

        small_2016 = selenium_tool.driver.find_element_by_xpath(
            "//figcaption[contains(text(), '2016')]/preceding-sibling::a/img"
        ).get_attribute('src')

        small_2012 = selenium_tool.driver.find_element_by_xpath(
            "//figcaption[contains(text(), '2012')]/preceding-sibling::a/img"
        ).get_attribute('src')
    except NoSuchElementException as e:
        print(e)
    finally:
        df_area.loc[index, 'big_area'] = big_area
        df_area.loc[index, '2020_small'] = small_2020
        df_area.loc[index, '2016_small'] = small_2016
        df_area.loc[index, '2012_small'] = small_2012

        big_area = ""
        small_2020 = ""
        small_2016 = ""
        small_2012 = ""

    index += 1

df_area.to_excel('选取地图_2.xlsx')


