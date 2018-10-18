#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  html_downloader.py
@Time    :  2018/10/17 20:18
"""
from urllib import request

''' 网页下载器 '''

class HtmlDownloader(object):

    def download(self, url):
        # 判断
        if url is None:
            print('url is None')
            return None
        # 否则
        response = request.urlopen(url)

        if response.getcode() != 200:   # 若请求失败
            print("response != 200")
            return None

        return response.read()          # 返回下载好的内容
