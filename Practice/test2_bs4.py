#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  test2_bs4.py
@Time    :  2018/10/16 20:56
"""
import re
from bs4 import BeautifulSoup

# 以下示例来自网站 https://www.crummy.com/software/BeautifulSoup/bs4/doc/
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# 创建 soup 对象
# 第一个参数指定为文档字符串 html_doc
# 第二个参数指定为 html.parsar 作为它的解析器
# 第三个参数指定编码为 utf-8
# soup = BeautifulSoup(html_doc, 'html.parsar', from_encoding='utf-8') # 不支持 Python 3.6
soup = BeautifulSoup(html_doc, 'lxml')

# 提取出所有的链接
print('获取所有的链接')
links = soup.find_all('a')
for link in links:
    # 打印出节点的名称，href属性以及节点的文字
    print(link.name, link['href'], link.get_text())

print('获取 Lacie 的链接')
link_node = soup.find('a', href='http://example.com/lacie')
print(link_node.name, link_node['href'], link_node.get_text())

print('正则匹配')
link_node = soup.find('a', href=re.compile(r'ill'))
print(link_node.name, link_node['href'], link_node.get_text())

print('获取 p 段落文字')
p_node = soup.find('p', class_='title')
print(p_node.name, p_node.get_text())

print('-' * 50)
print(soup.prettify())
