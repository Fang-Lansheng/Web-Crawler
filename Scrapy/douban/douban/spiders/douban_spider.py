# -*- coding: utf-8 -*-

import re
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

        # 获取数据 （Responses）
        # 循环电影的条目
        movie_list = response.xpath('//*[@id="content"]/div/div[1]/ol/li')

        for i_item in movie_list:
            # 将 items 文件导入进来
            douban_item = DoubanItem()

            # 写详细的 XPath，进行数据解析
            # 电影排名
            douban_item['ranking_number'] = i_item.xpath('./div/div[1]/em/text()').extract_first()

            # 电影名称
            douban_item['movie_title'] = i_item.xpath('./div/div[2]/div[1]/a/span[1]/text()').extract_first()

            # 电影职员表
            staff = i_item.xpath('./div/div[2]/div[2]/p[1]/text()').extract_first()
            douban_item['movie_staff'] = ' '.join(staff.split())

            # 电影标签
            tags = i_item.xpath('./div/div[2]/div[2]/p[1]/text()').extract()
            douban_item['movie_tag'] = ' '.join(tags[1].split())

            # 电影评分
            douban_item['movie_score'] = i_item.xpath('./div/div[2]/div/div/span[2]/text()').extract_first()

            # 电影评论人数
            comments = i_item.xpath('./div/div[2]/div/div/span[4]/text()').extract_first()  # 得到字符串“***人评价”，需要提取数字
            douban_item['movie_comments'] = (re.findall(r'\d+', comments))[0]

            # 电影引用
            douban_item['movie_quote'] = i_item.xpath('./div/div[2]/div/p[2]/span/text()').extract_first()

            # 电影 URL
            douban_item['movie_url'] = i_item.xpath('./div/div[2]/div[1]/a/@href').extract_first()

            # 需要将数据 yield 到 pipelines 中去，进行数据清洗和存储等
            yield douban_item

        # 新的请求 （Requests）
        # 解析下一页规则，取后页的 XPath
        link_next = response.xpath('//span[@class="next"]/link/@href').extract()
        if link_next:
            link_next = link_next[0]
            yield scrapy.Request("https://movie.douban.com/top250"+link_next, callback=self.parse)

