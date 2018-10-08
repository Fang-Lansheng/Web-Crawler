#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :  Thistledown
@Contact :  120768091@qq.com
@Software:  PyCharm
@File    :  cookie.py.py
@Time    :  2018/10/8 22:24
"""

from selenium import webdriver
import re
import time
import json
import urllib
import urllib3
import requests

'''
【爬取好友的说说信息】
爬取思路：
> 先使用 selenium 登录自己的 QQ 获取 cookies
> 将 cookies 传入 requests
> 找到所有好友的 QQ 号
> 通过构造 url 对好友的信息进行爬取
'''

# 使用 selenium 登录
def login():
    chrome_driver = 'D:/Software/Chrome/ChromeDriver/chromedriver.exe'
    driver = webdriver.Chrome(chrome_driver)
    # 打开 QQ 网页
    driver.get('https://i.qq.com/')
    driver.switch_to_frame('login_frame')
    # 利用 QQ 快速安全登录
    driver.find_element_by_id('img_out_120768091').click()
    time.sleep(5)
    # 得把 Frame 的定位换回来，否则可能会出错
    driver.switch_to.default_content()
    return driver

# 获取 cookies，返回带cookies的requests
def back_session(driver):
    my_session = requests.sessions()
    cookies = driver.get_cookies()
    cookie = {}

login()
