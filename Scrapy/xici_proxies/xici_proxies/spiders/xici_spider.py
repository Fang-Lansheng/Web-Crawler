# -*- coding: utf-8 -*-

import re
import scrapy
from xici_proxies.items import XiciProxiesItem


class XiciSpiderSpider(scrapy.Spider):
    # 爬虫名
    name = 'xici_spider'
    # 允许的域名
    allowed_domains = ['www.xicidaili.com']
    # 入口 URL
    start_urls = ['http://www.xicidaili.com/nn/1']

    def parse(self, response):

        proxy_list = response.xpath('//*[@id="ip_list"]/tbody/tr[position()>1]')

        for item in proxy_list:
            xici_item = XiciProxiesItem()

            ip = item.xpath('./td[2]/text()').extract_first()
            port = item.xpath('/td[3]/text()').extract_first()
            scheme = item.xpath('/td[6]/text()').extract_first()

            xici_item['IP'] = ip
            xici_item['port'] = port
            xici_item['scheme'] = scheme
            xici_item['URL'] = scheme + '://httpbin.org/ip'
            xici_item['proxy'] = scheme + '://' + ip + ':' + port

            meta = {'proxy': xici_item['proxy'],
                    'dont_retry': True,
                    'download_timeout': 30,
                    '_proxy_scheme': xici_item['scheme'],
                    '_proxy_ip': xici_item['IP']}

            if self.check_available(xici_item['IP']):
                yield xici_item

    def check_available(self, ip):
        if True:
            return True

