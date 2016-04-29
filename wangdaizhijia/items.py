# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WangdaizhijiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pm = scrapy.Field() #排名
    ptmc = scrapy.Field() #平台名称
    cjl = scrapy.Field() #成交量
    pjll = scrapy.Field() #平均利率
    pjjkqx = scrapy.Field() # 平均借款期限
    ljdhje = scrapy.Field() #累计待还金额
    # pass
