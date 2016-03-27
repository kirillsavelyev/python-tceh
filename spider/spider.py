import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst



class CustomPipeLine(object):
    pass

# scrapy spider.py -o file.json -t json


class Product(scrapy.Item):
    name = scrapy.Field(output_processor=TakeFirst())
    consist = scrapy.Field()


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']

    # custom_settings = {}

    def parse(self, response):
        for url in response.css('ul li a::attr("href")').re('.*/category/.*'):
            yield scrapy.Request(response.urljoin(url), self.parse_titles)

    def parse_titles(self, response):
        # for post_title in response.css('div.entries > ul > li a::text').extract():
        #     yield {'title': post_title}
        l = ItemLoader(item=Product(), response=response)
        l.add_css('name', '#content > h1::text')
        l.add_css('consist', 'div.entries > ul > li a::text')
        return l.load_item()
