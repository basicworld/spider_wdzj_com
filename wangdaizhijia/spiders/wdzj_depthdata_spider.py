# -*- coding: utf-8 -*-
import scrapy
import urllib
import time
from wangdaizhijia.items import WangdaizhijiaItem

# frmdata = {"id": "com.supercell.boombeach", "reviewType": 0, "reviewSortOrder": 0, "pageNum":0}
#         url = "https://play.google.com/store/getreviews"
#         yield Request(url, callback=self.parse, method="POST", body=urllib.urlencode(frmdata))

class WangdaizhijiaSpider(scrapy.Spider):
    name = "wdzj_depthdata"
    allowed_domains = ["wdzj.com"]
    start_urls = [
        "http://shuju.wdzj.com/platdata-1.html", # 从这里解析depth_data需要的wdzjPlatId
    ]

    def parse(self, response):
        """post"""
        for sel in response.xpath('//*[@id="tb_content"]/div[3]/table/tbody/tr'):
            response_url = sel.xpath('td[2]/a[1]/@href').extract()[0]
            wdzjPlatId = response_url.split('.')[0].split('-')[-1]
            url = 'http://shuju.wdzj.com/depth-data.html' #response.urljoin(href.extract())
            headers = {
                'Host': 'shuju.wdzj.com',
                # 'Connection': 'keep-alive',
                'Accept': '*/*',
                'Origin': 'http://shuju.wdzj.com',
                'X-Requested-With': 'XMLHttpRequest',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'DNT': '1',
                'Referer': 'http://shuju.wdzj.com/plat-info-%s.html'%(wdzjPlatId),
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
            }
            for (type1, type2) in [(1,2), (3,4),(5,6),(7,8),(9,10),(11,12),(15,0),(16,0),(17,0),(18,0)]:
                post_data = {'wdzjPlatId':str( wdzjPlatId),
                    'type1':str(type1),
                    'type2':str(type2),
                    'status':str(1),
                }
                # wdzjPlatId=60&type1=1&type2=2&status=0
                meta = {'filename': post_data['wdzjPlatId']+'_'+post_data['type1']+'_'+post_data['type2']+'.json',}
                yield scrapy.Request(url, method="POST", meta=meta, headers=headers, body=urllib.urlencode(post_data), callback=self.after_post)
                # request.meta['filename'] = post_data['wdzjPlatId']+'_'+post_data['type1']+'_'+post_data['type2']+'.json'
                # yield request

    def parse2(self, response):
        pass

    def after_post(self, response):

        filename = response.meta['filename']

        # filename = response.url.split("/")[-2] + str(time.time())+ '.json'
        # print filename
        with open(filename, 'wb') as f:
            f.write(response.body)
        print filename
