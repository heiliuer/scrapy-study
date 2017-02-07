#!/usr/bin/env python
# -*- coding: utf-8 -*-
import scrapy


# 获取腾讯新闻头条
class NewsSpider(scrapy.Spider):
    name = "qqnews"
    start_urls = [
        "http://news.qq.com/",
    ]

    def parse(self, response):
        titles = response.xpath(
            '/html/body/div[6]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/div/em/a/text()').extract()
        print "################"
        print "\n".join(title for title in titles)
        print "################"
