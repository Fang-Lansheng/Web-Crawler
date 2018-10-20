#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  main.py
@Time    :  2018/10/20 15:11
"""
''' 启动文件 '''
from scrapy import cmdline
cmdline.execute('scrapy crawl xici_proxies'.split())
