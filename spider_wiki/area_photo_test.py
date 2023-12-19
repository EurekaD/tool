import pandas as pd
from selenium_tool.selenuim_tool import SeleniumTool
from selenium.common.exceptions import NoSuchElementException

url = "https://zh.wikipedia.org/zh-hans/%E8%87%BA%E5%8C%97%E5%B8%82%E7%AC%AC%E5%9B%9B%E9%81%B8%E8%88%89%E5%8D%80_(%E7%AB%8B%E6%B3%95%E5%A7%94%E5%93%A1)"
selenium_tool = SeleniumTool()
selenium_tool.open_web(url)

try:
    p1 = selenium_tool.driver.find_element_by_xpath(
        "//div[@class='mw-content-ltr mw-parser-output']/p[1]").get_attribute('innerText')
    p2 = selenium_tool.driver.find_element_by_xpath(
        "//div[@class='mw-content-ltr mw-parser-output']/p[2]").get_attribute('innerText')
    p3 = selenium_tool.driver.find_element_by_xpath(
        "//div[@class='mw-content-ltr mw-parser-output']/p[3]").get_attribute('innerText')

    big_area = selenium_tool.driver.find_element_by_xpath(
        "//*[@id='mw-content-text']/div[1]/table[1]/tbody/tr[4]/td/span/a/img"
    ).get_attribute('src')
    print(big_area)

    small_2020 = selenium_tool.driver.find_element_by_xpath(
        "//figcaption[contains(text(), '2020')]/preceding-sibling::a/img"
    ).get_attribute('src')

    print(small_2020)

    small_2016 = selenium_tool.driver.find_element_by_xpath(
        "//figcaption[contains(text(), '2016')]/preceding-sibling::a/img"
    ).get_attribute('src')

    small_2012 = selenium_tool.driver.find_element_by_xpath(
        "//figcaption[contains(text(), '2012')]/preceding-sibling::a/img"
    ).get_attribute('src')
except NoSuchElementException as e:
    print(e)

