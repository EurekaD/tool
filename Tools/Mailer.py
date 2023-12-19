'''
@File: Mailer.py
@Copyright: Guanchang3
@Date: 2022/9/26
@Desc:
'''

import time

from scrapy.mail import MailSender

'''
@def: 添加在pipeline的close_spider方法下, 记得使用return传递避免io错误
@iteritem: 计数器，传递爬虫获取的新闻条数
@name: 爬虫名称，使用spider.name获取
'''
def send_email(iteritem, name):
    # 若放在spider中可以使用settings配置
    # mailer = MailSender.from_settings(spider.settings)
    create_time = time.strftime("%Y-%m-%d", time.localtime())
    mailer = MailSender(
        # smtp配置信息
        smtphost='smtp.exmail.qq.com',
        mailfrom='yjy@softline.sh.cn',
        smtpuser='yjy@softline.sh.cn',
        smtppass='Yangjiayi123',
        smtpport=465,
        smtpssl='True',
        smtptls='False'
    )
    body_c = "您已获取了" + str(iteritem) + "条" + name + "相关的新闻"
    return mailer.send(to=["dyj@softline.sh.cn"], subject=create_time + " " + name, body=body_c)

