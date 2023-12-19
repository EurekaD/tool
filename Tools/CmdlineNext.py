'''
@File: Cmdline.py
@Copyright: Guanchang3
@Date: 2022/8/15
@Desc: 调试用
'''
from scrapy import cmdline
# cmdline.execute("cd D:\\Workplace\\pyworkplace\\xd-spiders\\UnionNews")
# name = 'chdtv'
# name = 'newslens'
# cmd = 'scrapy crawl {0}'.format(name)
# cmdline.execute(cmd.split())
import os

def cmd_exec():
    folder_list = ['Chinatimes', 'ETtoday', 'LibertyTimesNet', 'Mirrormedia', 'Setnews', 'Thenewslens', 'TVBSnews', 'UnionNews']

    for folder in folder_list:
        fpath = f"D:\\Workplace\\pyworkplace\\xd-spiders\\{folder}"
        cmdline.execute(("cd "+fpath).split())
        command = "scrapy list"
        res = os.popen(command).readlines()
        for line in res:
            line = line.strip('\r\n')
            print(line)

if __name__ == '__main__':
    cmd_exec()
