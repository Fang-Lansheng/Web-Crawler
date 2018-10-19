# Scrapy 框架

###### 课程地址：[Python最火爬虫框架Scrapy入门与实践](https://www.imooc.com/learn/1017)

`2018年10月18日` `Python爬虫` `Scrapy`

---
[TOC]

## 课程内容
**开发环境：**
> Windows 10，Python 3.6，Scrapy 1.5，MongoDB 3.6，PyCharm

**适用人群：**

> 1. 具有一定的 Python 基础
> 2. 具有一定的 Linux 系统管理基础（编译安装软件、Yum 包管理工具等）
> 3. 具有一定的 Mongodb 数据库管理基础（增删改查）



**课程大纲：**

- Scrapy 介绍
- Scrapy 的安装
- Scrapy 在安装时经常遇到的问题
- MongoDB 的安装
- Scrapy 框架、组件、数据流
- Scrapy 数据抓取实战



### 一、Scrapy 安装

[安装指南 — Scrapy 1.0.5 文档](https://scrapy-chs.readthedocs.io/zh_CN/1.0/intro/install.html)

**方法一：使用 pip 安装**

```powershell
pip install scrapy
```

**方法二：Anaconda**

```powershell
conda install -c scrapinghub scrapy
```



### 二、Scrapy

#### 没有 Scarpy 的时候，我们怎么做数据抓取？

- `urllib` 或 `requrests`
- 多线程或协程
- 封装 http 头部信息类
- 封装代理类
- 数据去重类
- 封装数据存储类
- 封装异常检测机制
- …

#### Scrapy 是什么？

> Scrapy 是一套基于 Twisted 的异步处理框架，是纯 Python 实现的爬虫框架，用户只需要定制开发几个模块就可以轻松地实现一个爬虫，用来抓取网页内容或者各种图片

- 架构清晰
- 模块间耦合度低
- 可扩展性强

#### Scrapy 框架

![Scrapy框架](http://ww1.sinaimg.cn/large/006y42ybly1fwcosp9vccj30q30hzq7r)

- Scrapy Engine —— 引擎，负责其他四部分中间的通讯、信号和数据的传递
- Scheduler —— 调度器，（可以看成一个队列）队列，负责接收引擎发送的 requests 请求，然后将请求排队；当引擎需要请求数据的时候，就将请求队列中的数据交给引擎
- Downloader —— 下载器，负责发送请求并下载数据，负责下载引擎发送过来的所有 requests 请求，并将其获得的 responses 交还给引擎，然后再由引擎将 responses 交还给 Spiders 来进行解析
- Spiders —— 爬虫，其中有很多解析策略，用于分析和提取数据（items），负责处理所有的 responses，如果 responses 中有其他的请求，比如说下载某个链接时，Spider 会将 URL 交还给引擎，由引擎将这些 URL 再次交给调度器（Scheduler）
- Item Pipeline —— 管道，封装去重类、存储类，负责处理 Spider 中获取到的数据，并且进行后期处理、过滤以及存储等等
- Downloader Middleware —— 下载中间件，自定义扩展组件，封装代理或 http 头，用于隐藏自己
- Spider Middleware —— 爬虫中间件，自定义扩展引擎和 Spider 中间通信功能的组件，如进入 Spider 中的 responses 和 从 Spider 中出去的 requests 可以由其修改



### 三、MongoDB的安装

安装教程🔗：[Windows 平台安装 MongoDB | 菜鸟教程](https://www.runoob.com/mongodb/mongodb-window-install.html)

> **MongoDB 安装包**
>
> 下载地址：https://www.mongodb.com/download-center/v2/community
>
> 百度云镜像：
>
> - 链接：https://pan.baidu.com/s/1IeVY4B3XN0HT9XvpGiOtEQ
> - 提取码：mzii



### 四、Scrapy 项目实践

**Scrapy抓取 4 步走：**

- 新建项目
- 明确目标
- 制作爬虫
- 存储内容

#### 新建项目

```powershell
> $ scrapy startproject douban
New Scrapy project 'douban', using template directory 'd:\\software\\python\\anaconda\\anaconda3\\lib\\site-packages\\scrapy\\templates\\project', created in:
    D:\MyStuff\Git\Web-Crawler\Scrapy\douban

You can start your first spider with:
    cd douban
    scrapy genspider example example.com
```

生成爬虫文件

```powershell
> $ cd douban
> $ scrapy genspider douban_spider movie.douban.com
Created spider 'douban_spider' using template 'basic' in module:
  douban.spiders.douban_spider
```

#### 明确目标

打开链接

> https://movie.douban.com/top250

抓取豆瓣电影 TOP250 数据，并将数据保存为 `csv.json` ，存储到 MongoDB 数据库中。

需要获取的数据有：

- 电影排行
- 电影名称、介绍
- 电影星级、评价
- …



#### 制作爬虫

启动项目

```powershell
> $ scrapy crawl douban_spider.py
```



#### 存储内容

数据导出

```powershell
> $ scrapy crawl douban_spider -o test.json
> $ scrapy crawl douban_spider -o test.csv
```





