import pandas as pd
from selenium_tool.selenuim_tool import SeleniumTool
from selenium.common.exceptions import NoSuchElementException


df_edu = pd.DataFrame(columns=['name', 'time', 'href', 'color', 'photo'])


url = "https://flo.uri.sh/visualisation/13327660/embed"
selenium_tool = SeleniumTool()

selenium_tool.open_web(url)

time = ''
name = ''
href = ''
color = ''
src = ''


selenium_tool.wait_element("//div[@class='content-container']")
div_list = selenium_tool.driver.find_elements_by_xpath("//div[@class='content-container']/div[@class='content']")
selenium_tool.wait_and_click("//*[@id='fl-layout-primary']/div/div[2]/div")
index = 0
for div in div_list:
    try:
        time = div.find_element_by_xpath("./div[@class='content_inner']/div/p").get_attribute('innerText')
        name = div.find_element_by_xpath("./div[@class='content_inner']/p/span").get_attribute('innerText')
        href = div.find_element_by_xpath("./div[@class='content_inner']/p/span/a").get_attribute('href')
    except NoSuchElementException:
        pass
    finally:
        index += 1
        df_edu.loc[index, 'time'] = time
        df_edu.loc[index, 'name'] = name
        df_edu.loc[index, 'href'] = href
        print(time)
        print(name)
        print(href)



# for index in range(1, 33):
#     try:
#         div = selenium_tool.driver.find_element_by_xpath("//div[@id='content-{}']".format(index))
#         time = div.find_element_by_xpath("./div[@class='content_inner']/div/p").get_attribute('innerText')
#         name = div.find_element_by_xpath("./div[@class='content_inner']/p/span").get_attribute('innerText')
#         href = div.find_element_by_xpath("./div[@class='content_inner']/p/span/a").get_attribute('href')
#         df_edu.loc[index-1, 'time'] = time
#         df_edu.loc[index - 1, 'name'] = name
#         df_edu.loc[index - 1, 'href'] = href
#         print(time)
#         print(name)
#         print(href)
#     except NoSuchElementException:
#         pass


g_list = selenium_tool.driver.find_elements_by_xpath("//*[@class='markers']/*[@class='marker-group']")
index = 0
for g in g_list:
    # print(g.get_attribute('outerHTML'))
    try:
        src = g.find_element_by_xpath("./*[@x='0']").get_attribute('href')
        color = g.find_element_by_xpath("./*[@class='marker-background']").get_attribute('fill')
    except NoSuchElementException:
        pass
    finally:
        index += 1
        df_edu.loc[index, 'photo'] = src
        df_edu.loc[index, 'color'] = color
        print(src)
        print(color)

df_edu.to_excel('大事记录.xlsx')


