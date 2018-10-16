



# 学习笔记

课程地址：
[Python开发简单爬虫_python爬虫入门教程_python爬虫视频教程-慕课网](https://www.imooc.com/learn/563)  

---

[TOC]

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

  - 防止重复抓取、循环抓取
    - 不同的URL之间存在着循环指向的问题，如果不进行管理，爬虫就会循环抓取重复的URL

![](https://ws1.sinaimg.cn/large/006y42ybly1fwa45e7omqj30zq0dbq89.jpg)

- 实现方式：
  - 存储在内存中（个人、小型数据库）
  - 存储在关系数据库中（内存不足或永久保存）
  - 存储在缓存数据库中（大型公司）
	![](https://ws1.sinaimg.cn/large/006y42ybly1fwa4z9sa5mj30jx084412.jpg)

## 三、网页下载器

- 网页下载器：将互联网上URL对应的网页下载到本地的工具（类似于网页浏览器？）![](https://ws1.sinaimg.cn/large/006y42ybly1fwa49si2k3j30v908igpo.jpg)
- Python有哪几种网页下载器？![](https://ws1.sinaimg.cn/large/006y42ybly1fwa4f1fcvoj30it0c5ac3.jpg)
  - urllib2 —— Python官方的基础模块
    - 支持直接的URL下载
    - 支持向网页提交一些需要用户输入的数据
    - 支持需要登陆网页的cookie处理、需要代理访问的代理处理等增强功能
  - requests —— Python第三方的插件
    - 提供更为强大的功能



- 网页下载器 —— urllib2

  - urllib2下载网页方法1：最简洁方法![](https://ws1.sinaimg.cn/large/006y42ybly1fwa4gb1ln5j30cz0ait9m.jpg)

    ```python
    import urllib2
    
    # 直接请求
    response = urllib2.urlopen('https://www.baidu.com')
    
    # 获取状态码，如果是 200 表示获取成功
    print(response.getcode())
    
    # 读取内容
    cont = response.read()
    ```

  - urllib下载网页方法2：添加data、http header

    - data（向服务器提交需要用户输入的数据）
    - header（向服务器提交http的头信息）
    - 以request作为参数发送网页请求

    ![](https://ws1.sinaimg.cn/large/006y42ybly1fwa4ko7jzwj30ii0co0vo.jpg)

    ```python
    import urllib2
    
    # 创建 Request 对象
    request = urllib2.Request(url)
    
    # 添加数据
    request.add_data('a', '1')
    
    # 添加http的header
    request.add_header('user-agent', 'Mozilla/5.0')
    
    # 发送请求获取结果
    response = urllib2.urlopen(request)
    ```

  - urllib2下载放野方法3：添加特殊情景的处理器

    - HTTPCookieProcessor：有些网页需要用户登录才能访问，需要添加cookie的处理
    - ProxyHandler：有些网页需要代理才能访问
    - HTTPSHandler：有些网页的协议使用https加密访问
    - HTTPRedirectHandler：url之间存在相互、自动的跳转关系
    - 这些handler传送给build_opener，然后给urllib2来install_opener

    ![](https://ws1.sinaimg.cn/large/006y42ybly1fwa4szisb7j310o0e3n26.jpg)

    ```python
    import urllib2, cookielib	# 增强对 cookie 的处理
    
    # 创建cookie容器
    cj = cookielib.CookieJar()
    
    # 创建一个opener
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    
    # 给urllib2安装opener
    urllib2.install_opener(opener)
    
    # 使用带有cookie的urllib2访问网页
    response = urllib2.urlopen('http://www.badu.com/')
    ```

## 网页解析器

- 网页解析器：从网页中提取有价值数据的工具

  - 作用：
    - 提取出新的待爬取URL列表
    - 解析出有价值的数据

  ![](https://ws1.sinaimg.cn/large/006y42ybly1fwaa46zzo9j31050ejjvf.jpg)

- Python 有哪几种网页解析器？

  ![1539690463196](C:\Users\Thistledown\AppData\Roaming\Typora\typora-user-images\1539690463196.png)

  - 正则表达式 —— 最直观的一种
    - 将整个网页文档当成一个字符串，用正则表达式进行模糊匹配提取出所需要的数据
    - 虽然直观，但在文档复杂、庞大时非常麻烦
  - html.parser —— Python 自带模块
    - 可使用 html.parser 或者 lxml（更强大）作为其解析器
  - Beautiful Soup —— 第三方插件
  - lxml —— 第三方插件（解析 html/xml 网页）

- 结构化解析 - DOM（Document Object Model）树

  - 将整个网页文档加载成一个DOM树（文档对象模型），以树的方式进行上下级元素的遍历和访问
  - DOM树

  ![1539690919467](C:\Users\Thistledown\AppData\Roaming\Typora\typora-user-images\1539690919467.png)

- Beautiful Soup

  - Python 第三方库，用于从 HTML 或 XML 中提取数据
  - 官网：http://www.crummy.com/software/BeautifulSoup
  - 安装并测试 beautifulsoup4
    - 安装：`pip install beautifulsoup4`
    - 测试：`import bs4`
    - 