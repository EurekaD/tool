'''
@File: Cmdline.py
@Copyright: Guanchang3
@Date: 2022/8/15
@Desc: 调试用
'''
from scrapy import cmdline
# cmdline.execute("cd D:\\Workplace\\pyworkplace\\xd-spiders\\UnionNews")
# name = 'chdtv'
name = 'chdtv'
cmd = f'scrapy crawl {name}'
cmdline.execute(cmd.split())