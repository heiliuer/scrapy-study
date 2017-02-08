python 爬虫框架 scrapy 学习源码

> 当前scrapy版本 1.3.0 （不支持python3）

> [官方文档](https://doc.scrapy.org/en/1.3)

> [中文文档](http://scrapy-chs.readthedocs.io/zh_CN/0.24/index.html)

- 安装
    
    - windows
        
        - 安装配置 python2.7 （< 2.7.9 python版本需要手动安装pip），并配置python2.7到环境变量
        
            `set path=C:\Python27;C:\Python27\Scripts;%path%`
        
        - 安装 Scrapy
            
            `pip install Scrapy`
        
            > 安装会报 lxml依赖 错误
            
            - 下载lxml egg安装文件 https://pypi.python.org/packages/d4/fa/e4e0c7a8fe971b10e275cdc20efd16f553a225e700c400c11da25276e4f4/lxml-2.3-py2.7-win32.egg#md5=607f701d0961834667abe737b3206215
            
                `easy_install lxml-2.3-py2.7-win32.egg`
        - 再次安装 Scrapy
        
            `pip install Scrapy`
            
        - 运行爬虫包win32api错误,安装pypiwin32
        
            `pip install pypiwin32`
       
    - ubuntu 16.04 
    
        - 安装 python2.7 和 pip
        
        - 安装依赖
        
            `sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev`
        
        - 安装 Scrapy
            
            `pip install Scrapy`
    
    - 树莓派3（官方系统 Raspbian）
    
        sudo apt-get install libffi-dev libxml2-dev libxslt1-dev python-dev
        
        sudo pip install scrapy
        
      > 树莓派 arm gcc 编译有些慢，耐心等候5分钟

- 测试是否安装成功
        
        `bash#python`
        `>>>import scrapy`
        
    > 不报错，说明scrapy安装成功
    

- scrapy 命令行工具

    > scrapy 安装成功后，命令行程序路径位于 `<python安装目录>/Scripts/scrapy.exe`
    
    测试 scrapy 命令 (`<python安装目录>/Scripts/` 需加入环境变量path)

        E:\Projects\my-githubs\scrapy-study\001hello-world>scrapy
        Scrapy 1.3.0 - project: hello
        
        Usage:
          scrapy <command> [options] [args]
        
        Available commands:
          bench         Run quick benchmark test
          check         Check spider contracts

- scrapy 命令行新建项目

    `scrapy startproject hello .`
    
    scrapy 会在当前目录建立如下文件结构
    
        │  scrapy.cfg
        │
        └─hello
            │  items.py
            │  middlewares.py
            │  pipelines.py
            │  settings.py
            │  __init__.py
            │
            └─spiders
                    __init__.py
    
- 运行 spider
    
    `scrapy crawl [options] <spider>`
    

- pystorm 调试

    [参考](http://www.07net01.com/2015/08/904875.html)
    
    `C:\Python27\python.exe C:/Python27/Lib/site-packages/scrapy/cmdline.py crawl --nolog qqnews`          