#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  html_parser.py
@Time    :  2018/10/17 20:18
"""
''' 网页解析器 '''

import re
from urllib import request
from bs4 import BeautifulSoup

class HtmlParser(object):

    def parse(self, page_url, html_cont):
        '''
        需要从网页内容中解析出新的 URL 列表和数据
        :param page_url:    页面 URL
        :param html_cont:   网页内容
        :return:
        '''
        if page_url is None or html_cont is None:
            print('page_url is None or html_cont is None')
            return

        soup = BeautifulSoup(html_cont, 'html.parser')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()

        # 匹配出所有词条的 URL
        # /item/%E9%98%BF%E5%A7%86%E6%96%AF%E7%89%B9%E4%B8%B9/2259975
        links = soup.find_all('a', href=re.compile(r'/item/[0-9a-zA-Z%/]+'))
        for link in links:
            new_url = link['href']
            new_full_url = request.urljoin('https://baike.baidu.com', new_url)
            new_urls.add(new_full_url)
        return new_urls


    def _get_new_data(self, page_url, soup):
        res_data = {}   # 存放数据的字典

        # url
        res_data['url'] = page_url

        # 得到标题的标签
        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1></dd>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()

        # 得到摘要
        # <div class="lemma-summary" label-module="lemmaSummary">***</div>
        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()

        return res_data
