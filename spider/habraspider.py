# -*- coding: utf-8 -*-

import scrapy
from scrapy.loader import ItemLoader
import json
import codecs
from scrapy.loader.processors import TakeFirst, Join

# scrapy runspider E:\Python\Repository\spider\habraspider.py -t json -a user_name=Lof


class JsonUTF8Pipeline(object):

    def __init__(self):
        self.file = codecs.open('habraspider_result.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()


class BlogCategory(scrapy.Item):
    hub = scrapy.Field(output_processor=TakeFirst())
    date = scrapy.Field(output_processor=TakeFirst())
    title = scrapy.Field(output_processor=TakeFirst())
    article = scrapy.Field(output_processor=Join())


class BlogSpider(scrapy.Spider):
    name = 'hubrspider'

    def __init__(self, post_date=u'18 февраля.*', user_name='imperituroard'):
        self.start_urls = ['https://habrahabr.ru/users/' + user_name]
        self.post_date = post_date

    custom_settings = {
        'ITEM_PIPELINES': {'habraspider.JsonUTF8Pipeline'}
    }

    def parse(self, response):
        for url in response.css('#hubs_data_items > li a::attr("href")').re(".*/hub/.*"):
            yield scrapy.Request(response.urljoin(url), self.parse_page)

    def parse_page(self, response):
        hub_name = response.css('title::text').extract()

        for post in response.css('.posts_list .post'):
            if post.css('div.published::text').re(self.post_date):
                for url in post.css('h1 a::attr("href")').extract():
                    yield scrapy.Request(response.urljoin(url), self.parse_titles, meta={'hname': hub_name})

        # Takes all pages of Hub
        for url in response.css('#next_page::attr("href")').re(".*/page.*"):
            if url:
                yield scrapy.Request(response.urljoin(url), self.parse_page)

    def parse_titles(self, response):
        loader = ItemLoader(item=BlogCategory(), response=response)
        loader.add_value('hub', response.meta['hname'])
        loader.add_css('title', 'div.company_post h1 span::text')
        loader.add_css('date', 'div.published::text')
        loader.add_css('article', 'div.content::text')
        yield loader.load_item()
