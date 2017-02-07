#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy.http import Request


# 获取腾讯新闻头条
class NewsSpider(scrapy.Spider):
    name = "duanzi"
    start_urls = [
        "http://m.neihanshequ.com",
        "http://m.neihanshequ.com/?is_json=1&app_name=neihanshequ_web&max_time=1486365256",
    ]

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
        "Connection": "keep-alive",
        "Cookie": "uuid=\"w:a67b5cda12154867ac4f4d4b094cc010\"; skip_guidence=1; csrftoken=22a08d7f81eda454c5495ada674e2036; tt_webid=54513104534",
        "Host": "m.neihanshequ.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Referer": "http://m.neihanshequ.com/"
    }

    def make_requests_from_url(self, url):
        return Request(url, dont_filter=True, cookies={'.neihanshequ.com': 'true', 'm.neihanshequ.com': 'true'})

    def parse(self, response):
        print "################"
        data = json.loads(response.body_as_unicode)
        print "################"
        print "################"
