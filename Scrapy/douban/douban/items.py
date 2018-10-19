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
    movie_introduction = scrapy.Field()     # 电影介绍
    movie_rating = scrapy.Field()           # 电影星级（⭐→⭐⭐⭐⭐⭐）
    movie_score = scrapy.Field()            # 电影评分（0-10）
    movie_quote = scrapy.Field()            # 电影引用（一句话评价）

