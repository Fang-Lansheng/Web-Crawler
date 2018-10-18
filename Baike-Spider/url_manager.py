#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  url_manager.py
@Time    :  2018/10/17 20:17
"""
''' URL 管理器 '''

class URLManager(object):
    def __init__(self):
        self.new_urls = set()   # set() 函数创建一个无序不重复元素集
        self.old_urls = set()

    # 向 URL 管理器中添加一个新的 URL
    def add_new_url(self, url):
        if url is None:
            print('url is None')
            return  # 不进行添加
        # 若该 URL 既不在待爬取的 URL 列表中，也不在爬取过的 URL 列表中
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)


    # 向 URL 管理器中批量添加 URL
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            print('url is None or len(urls) == 0')
            return
        for url in urls:
            self.add_new_url(url)

    # 判断管理器中是否有新的待爬取的 URL
    def has_new_url(self):
        return len(self.new_urls) != 0

    # 从 URL 管理器中获取一个新的待爬取的 URL
    def get_new_url(self):
        new_url = self.new_urls.pop()   # set.pop()方法用于随机移除一个元素并返回移除的元素
        self.old_urls.add(new_url)      # 已获取的 URL 添加至 old_url 中
        return new_url

