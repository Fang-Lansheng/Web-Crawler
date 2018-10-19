#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  scrapy_proxies.py
@Time    :  2018/10/19 20:50
"""
''' 为 Scrapy 提供代理服务 '''
import scrapy
from scrapy import Request
import json

# cmdline.execute('scrapy runspider scrapy_proxies.py -o .\\files\proxy.json'.split())


class XiciSpider(scrapy.Spider):
    name = 'xici'
    allowed_domains = ['xicidaili.com'] # 从 xicidaili.com 爬取代理 IP 地址
    start_urls = ['http://www.xicidaili.com/nn/1']

    def parse(self, response):
        for sel in response.xpath('//*[@id="ip_list"]/tbody/tr[position()>1]'):
            ip = sel.xpath('./td[2]/text()').extract_first()
            port = sel.xpath('./td[3]/text()').extract_first()
            scheme = sel.xpath('./td[6]/text()').extrac_first().lower()

            url = scheme + '://httpbin.org/ip'
            proxy = scheme + '://' + str(ip) + ':' + str(port)

            meta = {
                'proxy': proxy,
                'dont_retry': True,
                'download_timeout': 30,
                '_proxy_scheme': scheme,
                '_proxy_ip': ip
            }

            print('===>>> Proxy: ', proxy)
            yield Request(url, callback=self.check_available(response), meta=meta, dont_filter=True)
            yield meta

    def check_available(self, response):
        proxy_ip = response.meta['_proxy_ip']
        print(proxy_ip)
        # print(response.text)

        if proxy_ip == json.loads(response.text)['origin']:
            print('yield')
            yield {
                'proxy_scheme': response.meta['_proxy_scheme'],
                'proxy': response.meta['proxy']
            }
