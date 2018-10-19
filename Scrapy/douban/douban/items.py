# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 需要抓取的数据有：
    ranking_number = scrapy.Field()         # 电影排名
    movie_title = scrapy.Field()            # 电影名称
    movie_staff = scrapy.Field()            # 电影职员表（导演：...）
    movie_tag = scrapy.Field()              # 电影标签（年份/国家/类型）
    movie_score = scrapy.Field()            # 电影评分（0-10）
    movie_comments = scrapy.Field()         # 电影评论人数
    movie_quote = scrapy.Field()            # 电影引用（一句话评价）
    movie_url = scrapy.Field()              # 电影URL（豆瓣）

