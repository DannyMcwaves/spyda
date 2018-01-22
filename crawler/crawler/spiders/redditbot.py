# -*- coding: utf-8 -*-
__all__ = ['RedditbotSpider']

import scrapy


class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'
    allowed_domains = ['www.reddit.com/r/gameofthrones/']
    start_urls = ['http://www.reddit.com/r/gameofthrones//']

    def parse(self, response):
        print(response)
        title = response.css('title::text').extract_first()
        div = response.css('p::text').extract()
        return {
            'title': title,
            'div': div
        }
