#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  test_urllib2.py
@Time    :  2018/10/16 18:15
"""

# 在Python3.x 中使用 import urllib.request，urllib.error，对应在 Python2.x 中使用 import urllib2
import urllib.request
# python2中的 cookielib 改为 http.cookiejar
import http.cookiejar

url = 'http://www.baidu.com'

print('第一种方法')
response1 = urllib.request.urlopen(url)
print(response1.getcode())
print(len(response1.read()))

print('*' * 50)
print('第二种方法')
request = urllib.request.Request(url)
request.add_header('user-agent', 'Mozilla/5.0')
response2 = urllib.request.urlopen(request)
print(response2.getcode())
print(len(response2.read()))

print('*' * 50)
print('第三种方法')
cj = http.cookiejar.CookieJar() # 创建一个 cookie 的容器
cookieProcessor = urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(cookieProcessor) # 创建一个 opener
urllib.request.install_opener(opener)   # 安装 opener，此时 urllib 具有 cookie 处理的增强能力
response3 = urllib.request.urlopen(url)
print(response3.getcode())
print(cj)
print(response3.read())




