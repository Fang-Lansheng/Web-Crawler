# Baike-Spider 学习笔记

###### 课程地址：[Python开发简单爬虫_python爬虫入门教程_python爬虫视频教程-慕课网](https://www.imooc.com/learn/563)

`2018年10月18日` `Python爬虫` `urllib.request` `BeautifulSoup`

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

###  一、爬虫简介

- 爬虫：一段自动抓取互联网信息的程序
    - 爬虫可以从一个URL（统一资源定位器）出发，访问它所关联的所有的URL
    - 并且从每个页面上提取出我们所需要的、有价值的数据
![](https://ws1.sinaimg.cn/large/006y42ybly1fwa3qt3atpj31070d4wl3.jpg)
- 作用：收集数据、数据利用与分析
- 价值：互联网数据可以更好地使用
- 简单爬虫架构：
![](https://ws1.sinaimg.cn/large/006y42ybly1fwa3wbxapzj30zm0g1gpz.jpg)
    - 运行流程：![](https://ws1.sinaimg.cn/large/006y42ybly1fwa3ytibjwj311k0l9477.jpg)

###  二、URL管理器
- URL管理器：管理待抓取URL集合和已抓取URL集合

  - 防止重复抓取、循环抓取
    - 不同的URL之间存在着循环指向的问题，如果不进行管理，爬虫就会循环抓取重复的URL

![](https://ws1.sinaimg.cn/large/006y42ybly1fwa45e7omqj30zq0dbq89.jpg)

- 实现方式：
  - 存储在内存中（个人、小型数据库）
  - 存储在关系数据库中（内存不足或永久保存）
  - 存储在缓存数据库中（大型公司）
   ![](https://ws1.sinaimg.cn/large/006y42ybly1fwa4z9sa5mj30jx084412.jpg)

### 三、网页下载器

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
    import urllib2, cookielib  # 增强对 cookie 的处理
    
    # 创建cookie容器
    cj = cookielib.CookieJar()
    
    # 创建一个opener
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    
    # 给urllib2安装opener
    urllib2.install_opener(opener)
    
    # 使用带有cookie的urllib2访问网页
    response = urllib2.urlopen('http://www.badu.com/')
    ```

### 四、网页解析器

- 网页解析器：从网页中提取有价值数据的工具

  - 作用：
    - 提取出新的待爬取URL列表
    - 解析出有价值的数据

  ![](https://ws1.sinaimg.cn/large/006y42ybly1fwaa46zzo9j31050ejjvf.jpg)

- Python 有哪几种网页解析器？

  ![](https://ws1.sinaimg.cn/large/006y42ybly1fwacizcs0hj30yk0dwaf4.jpg)

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

  ![](https://ws1.sinaimg.cn/large/006y42ybly1fwaciqq0dpj310e0epn31.jpg)

- Beautiful Soup

  - Python 第三方库，用于从 HTML 或 XML 中提取数据
  - 官网：http://www.crummy.com/software/BeautifulSoup
  - 安装并测试 beautifulsoup4
    - 安装：`pip install beautifulsoup4`
    - 测试：`import bs4`
  - 语法：
    ![](https://ws1.sinaimg.cn/large/006y42ybly1fwaciezbtuj30tz0g143c.jpg)

    - 例如：  

      ![](https://ws1.sinaimg.cn/large/006y42ybly1fwafcuno2mj30yp0c7q6c.jpg)

    - 对应代码：

      ```python
      ### 创建 BeautifulSoup对象
      from bs4 import BeautifulSoup
      
      # 根据 HTML 网页字符串创建 BeautifulSoup 对象
      soup = BeautifulSoup(html_doc,            # HTML 文档字符串
                           'html.parser'         # HTML 解析器
                           from_encoding='utf-8'   # HTML 文档的编码
                          )
       
      ### 搜索节点（find_all, find）
      # 方法：find_all(name, attrs, string)
      
      # 查找所有标签为 a 的节点
      soup.find_all('a')
      
      # 查找所有标签为 a，链接符合 /view/123.htm 形式的节点
      soup.find_all('a', href='/view/123.htm')
      soup.find_all('a', href=re.complie(r'/view/\d+\.htm'))   # 也可以传入正则表达式，来匹配对应的内容
      
      # 查找所有标签为 div，class 为 abc，文字为 Python 的节点
      soup.find_all('div', class_='abc', string='Python')
      
      ### 访问节点信息
      # 得到节点： <a href='1.html'>Python</a>
      
      # 获取查找到的节点的标签名称
      node.name
      
      # 获取查找到的 a 节点的 href 属性
      node['href']
      
      # 获取查找到的 a 节点的链接文字
      node.get_text()
      ```

### 五、实例爬虫

![](https://ws1.sinaimg.cn/large/006y42ybly1fwaepikppcj30tp0elwi9.jpg)

- 确定目标
  - 抓取哪个网站的哪些网页的数据
- 分析目标：确定抓取网站数据的策略
  - 确定抓取目标页面的目标的格式，用于限定抓取目标的范围（URL格式）
  - 确定抓取数据的（所在标签的）格式
  - 分析页面的编码
- 编写代码：在代码的解析器部分使用到分析目标所得到的抓取策略的结果
- 执行爬虫

#### 实例爬虫 - 分析目标

- 目标：百度百科 Python 词条相关词条网页 - 标题和简介

- 入口页：https://baike.baidu.com/item/Python/407313?fr=aladdin

- URL格式：

  - 词条页面URL：`/item/%E9%98%BF%E5%A7%86%E6%96%AF%E7%89%B9%E4%B8%B9/2259975`
  - 这不是一个完整URL，需要在前面加上 `baike.baidu.com`

- 数据格式

  - 标题：

    ```html
    <dd class="lemmaWgt-lemmaTitle-title"><h1>***</h1></dd>
    ```

  - 简介：
    ```html
    <div class="lemma-summary" label-module="lemmaSummary">***</div>
    ```

  - 页面编码：`UTF-8`

## 编程过程中出现的问题

**1. 地址问题**

- Python 百度百科词条地址由 `https://baike.baidu.com/view/10812319.htm` （已锁定）改为如今的 https://baike.baidu.com/item/Python/407313?fr=aladdin
- 词条页面中出现的 URL 格式和教程中不一致，例如

```html
<a target="_blank" href="/item/%E9%98%BF%E5%A7%86%E6%96%AF%E7%89%B9%E4%B8%B9/2259975" data-lemmaid="2259975">阿姆斯特丹</a>
```

故修改 `html_parser.py` （解析器）中的正则表达式

```python
links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
```

为：

```python
links = soup.find_all('a', href=re.compile(r"/item/*"))
```

**2. 文件写入的问题**

输出文件时出现了如下错误：

> TypeError: write() argument must be str, not bytes

编译器报错，发现 `html_outputter.py` 中文件的打开方式存在问题：

```python
f_out = open('output.html', 'w')
```

通过查询资料（[Python3 File 方法 | 菜鸟教程](http://www.runoob.com/python3/python3-file-methods.html)）改为：

```python
f_out = open('output.html', 'wb+')	
# wb+：以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。（一般用于非文本文件如图片等）
```

之后出现新的错误：

> TypeError: a bytes-like object is required, not 'str'

根据编译器报错，发现写入文件时要以二进制写入，而非字符串（str），所以出错。因此在写入字符串时用 `b''` 将其强制转换为 bytes 字符节

例如：

```python
f_out.write(b'<!DOCTYPE html>')
```

终于，可以成功写入数据到 `output.html` 文件了，但是打开一看，发现中文字符乱码。通过在输出的 .html 文件修改 `<head>` 标签得以成功显示：

```html
<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8"><title>OUTPUT.html</title></head>
```

**3. 耗时问题**

程序运行时间非常长，因此我引入了 `time` 模块，输出运行时间：

> $ spider_main.py
>
> 【 爬虫程序开始 】	at 2018-10-18 18:42:15
> → craw 1 : https://baike.baidu.com/item/Python/407313?fr=aladdin in 4.175590753555298 s
> → craw 2 : https://baike.baidu.com/item/%E8%99%9A%E6%8B%9F%E6%9C%BA in 4.365839719772339 s
> → craw 3 : https://baike.baidu.com/item/OS in 7.095842123031616 s
> → craw 4 : https://baike.baidu.com/item/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%97%85%E6%AF%92 in 4.249522924423218 s
>
> … …
>
> → craw 998 : https://baike.baidu.com/item/%E7%99%BD%E7%A7%8B%E6%9E%97 in 0.24550580978393555 s
> → craw 999 : https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E4%BC%81%E4%B8%9A%E5%8F%91%E5%B1%95%E7%A0%94%E7%A9%B6%E4%B8%AD%E5%BF%83 in 0.2914268970489502 s
> → craw 1000 : https://baike.baidu.com/item/%E9%95%87%E5%AE%88%E4%BD%BF in 0.5757756233215332 s
> 【 程序结束 】	at 2018-10-18 19:19:48 
> --- 耗时： 2253.4674208164215 s ---

通过多次尝试，发现跑完一次程序的时间最快也在八分钟以上，固然和爬取数目（1000）有关，但同样受网速影响特别大，校园网抽风也不是一回两回了orz

**4. 其他问题**

跑完程序后，我仍然有一个疑惑：每回输出的 html 文件的内容都是不同的，也就是说每次爬取的都不完全是同样的页面，这个原因为何，是否存在影响因素，仍待后续探索。



