from bs4 import BeautifulSoup

from pdf_gen.selenium_get_html import GetHtml


def process(html_content):
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    for element in soup.descendants:
        print(element)

url = 'https://www.hk01.com/article/957244'
get_html = GetHtml()
html = get_html.get_html(url)

process(html)




