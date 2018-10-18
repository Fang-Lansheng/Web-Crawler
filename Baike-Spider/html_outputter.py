#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  html_output.py
@Time    :  2018/10/17 20:18
"""
''' HTML 输出器 '''

class HtmlOutputter(object):
    def __init__(self):
        self.html_data = []    # 列表，用于维护收集的数据

    # 收集数据
    def collect_data(self, data):
        if data is None:
            print('data is None')
            return
        self.html_data.append(data)

    # 将收集好的数据写出到一个 html 文件中
    def output_html(self):
        f_out = open('output.html', 'wb+')
        # wb+：以二进制格式打开一个文件用于读写。
        # 如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。
        # 如果该文件不存在，创建新文件。
        #（一般用于非文本文件如图片等）

        f_out.write(b'<!DOCTYPE html>'
                    b'<html lang="zh-CN">'
                    b'<head>'
                    b'<meta charset="utf-8">'
                    b'<title>OUTPUT.html</title>'
                    b'</head>'
                    b'<body>'
                    b'<table>')

        for data in self.html_data:
            f_out.write(b'<tr>')
            f_out.write(b'<td>')
            f_out.write(data['url'].encode('utf-8'))
            f_out.write(b'</td>')    # 闭合标签
            f_out.write(b'<td>')
            f_out.write(data['title'].encode('utf-8'))
            f_out.write(b'</td>')    # 闭合标签
            f_out.write(b'<td>')
            f_out.write(data['summary'].encode('utf-8'))
            f_out.write(b'</td>')    # 闭合标签
            f_out.write(b'</tr>')  # 闭合标签

        f_out.write(b'</table>'
                    b'</body>'
                    b'</html>')      # 闭合标签

        f_out.close()
