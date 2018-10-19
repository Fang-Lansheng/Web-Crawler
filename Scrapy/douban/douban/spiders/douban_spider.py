# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem


class DoubanSpiderSpider(scrapy.Spider):
    # 爬虫名（和项目名称不能重复）
    name = 'douban_spider'
    # 允许的域名，不包含在其中的域名不进行抓取
    allowed_domains = ['movie.douban.com']
    # 入口 URL，扔到调度器里面去
    start_urls = ['https://movie.douban.com/top250']    # 豆瓣电影 Top 250

    # 解析器
    def parse(self, response):
        # print(response.text)    # 打印出内容
        movie_list = response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for i_item in movie_list:
            print(i_item)   # 首页 25 个电影信息
            douban_item = DoubanItem()
            douban_item['ranking_number'] = i_item.xpath('./div/div[1]/em/text()').extract_first()
            print(douban_item)
