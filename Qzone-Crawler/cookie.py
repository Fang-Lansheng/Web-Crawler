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
from http import cookiejar
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
    # 将cookies转换为字典格式
    for elem in cookies:
        cookie[elem['name']] = elem['value']

    headers = {'host': 'user.qzone.qq.com',
               'accept-encoding': 'gzip, deflate, br',
               'accept-language': 'zh-CN,zh;q=0.9',
               'accept': '*/*',
               'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
               'connection': 'keep-alive'}
    c = requests.utils.cookiejar_from_dict(cookie, cookiejar=None, overwrite=True)
    my_session.headers = headers
    my_session.cookies.update(c)
    return  my_session

# g_tk 算法
def get_g_tk(cookie):
    hashes = 5381
    for letter in cookie['p_skey']:
        hashes += (hashes << 5) + ord(letter) # ord 是用来返回字符的 ASCII 码

    return hashes & 0x7fffffff

# 找出好友QQ号和备注列表
def get_friend(self):
    url_friend = 'https://user.qzone.qq.com/proxy/domain/r.qzone.qq.com/cgi-bin/tfriend/friend_ship_manager.cgi?'
    g_tk = self.get_g_tk()
    uin = self.get_uin()
    data = {'uin': uin,
            'do': 1,
            'g_tk': g_tk}
    data_encode = urllib.parse.urlencode(data)
    url_friend += data_encode
    res = requests.get(url_friend, headers=header, cookies=cookie)


back_session(login())
