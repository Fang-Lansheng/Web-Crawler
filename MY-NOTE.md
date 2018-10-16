# 学习笔记

课程地址：
[Python开发简单爬虫_python爬虫入门教程_python爬虫视频教程-慕课网](https://www.imooc.com/learn/563)  

## 课程内容
1. 爬虫简介
2. 简单爬虫架构
3. URL管理器
4. 网页下载器（urllib2）
5. 网页解析器（BeautifulSoup）
6. 完整实例
    - 爬取百度百科 *Python* 词条相关的1000个页面数据

## 一、爬虫简介
- 爬虫：一段自动抓取互联网信息的程序
    - 爬虫可以从一个URL（统一资源定位器）出发，访问它所关联的所有的URL
    - 并且从每个页面上提取出我们所需要的、有价值的数据
![](https://ws1.sinaimg.cn/large/006y42ybly1fwa3qt3atpj31070d4wl3.jpg)
- 作用：收集数据、数据利用与分析
- 价值：互联网数据可以更好地使用
- 简单爬虫架构：
![](https://ws1.sinaimg.cn/large/006y42ybly1fwa3wbxapzj30zm0g1gpz.jpg)
    - 运行流程：![](https://ws1.sinaimg.cn/large/006y42ybly1fwa3ytibjwj311k0l9477.jpg)

## 二、URL管理器
- URL管理器：管理待抓取URL集合和已抓取URL集合


