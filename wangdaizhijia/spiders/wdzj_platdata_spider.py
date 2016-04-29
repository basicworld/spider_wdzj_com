# -*- coding: utf-8 -*-
import scrapy

from wangdaizhijia.items import WangdaizhijiaItem

class WangdaizhijiaSpider(scrapy.Spider):
    name = "wdzj_platdata"
    allowed_domains = ["wdzj.com"]
    start_urls = [
        "http://shuju.wdzj.com/platdata-1.html",
    ]

    # def parse(self, response):
    #     for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
    #         url = response.urljoin(href.extract())
    #         yield scrapy.Request(url, callback=self.parse_dir_contents)

    # def parse(self, response):
    #     filename = response.url.split("/")[-2] + '.html'
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)

    def parse(self, response):
        for sel in response.xpath('//*[@id="tb_content"]/div[3]/table/tbody/tr'):
            item = WangdaizhijiaItem()
            item['pm'] = sel.xpath('td')[0].xpath('span/text()').extract()[0]
            item['ptmc'] = sel.xpath('td/a[@target="_blank"]/span/text()').extract()
            item['cjl'] = sel.xpath('td/text()').extract()[0]
            item['pjll'] = sel.xpath('td/text()').extract()[1]
            item['pjjkqx'] = sel.xpath('td/text()').extract()[2]
            item['ljdhje'] = sel.xpath('td/text()').extract()[3]
            yield item

            # pm = scrapy.Field() #排名
            # ptmc = scrapy.Field() #平台名称
            # cjl = scrapy.Field() #成交量
            # pjll = scrapy.Field() #平均利率
            # pjjkqx = scrapy.Field() # 平均借款期限
            # ljdhje = scrapy.Field() #累计待还金额
            # //*[@id="tb_content"]/div[3]/table/tbody