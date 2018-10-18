#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  spider_main.py
@Time    :  2018/10/17 20:17
"""
import html_downloader
import html_outputter
import html_parser
import url_manager
import time

''' 爬虫总调度程序 '''

# 编写 main 函数
class SpiderMain(object):
    def __init__(self):             # 在构造函数中初始化各个对象
        self.urls = url_manager.URLManager()                # URL 管理器
        self.downloader = html_downloader.HtmlDownloader()  # HTML 下载器
        self.parser = html_parser.HtmlParser()              # 网页解析器
        self.outputter = html_outputter.HtmlOutputter()     # 输出器

    def craw(self, root_url):       # 爬虫的调度程序
        count = 1                   # 记录当前爬取的是第几个 URL

        self.urls.add_new_url(root_url)             # 将 root_url 添加进 URL 管理器

        while self.urls.has_new_url():              # 当 URL 管理器中有获取的 URL 时
            try:
                new_url = self.urls.get_new_url()       # 获取 URL
                print('→ craw', count, ':', new_url)
                # 启动下载器下载页面，结果保存
                html_cont = self.downloader.download(new_url)
                # 用解析器来解析页面数据，得到新的 URL 列表以及新的数据
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)        # 将获取到的新的 URL 添加到 URL 管理器
                self.outputter.collect_data(new_data)   # 收集获取到的数据

                # 目标是爬取 1000 个页面
                if count < 5:
                    count = count + 1
                else:
                    break
            except:
                print('craw failed')                # 异常处理

        self.outputter.output_html() # 输出收集好的数据

if __name__ == '__main__':
    time_start = time.time()
    print('【 爬虫程序开始 】\tat', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

    root_url = 'https://baike.baidu.com/item/Python/407313?fr=aladdin'  # 入口 url
    obj_spider = SpiderMain()   # 创建 Spider
    obj_spider.craw(root_url)   # 用 craw() 方法启动爬虫

    print('【 程序结束 】\tat', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
          '\n--- 耗时：', time.time() - time_start, 's ---')


