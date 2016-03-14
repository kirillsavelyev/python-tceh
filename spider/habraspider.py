import scrapy
from scrapy.loader import XPathItemLoader
from scrapy.loader.processors import TakeFirst


class BlogCategory(scrapy.Item):
    date = scrapy.Field(output_processor=TakeFirst())
    title = scrapy.Field()
    article = scrapy.Field()


class BlogSpider(scrapy.Spider):
    name = 'hubrspider'
    start_urls = ['https://habrahabr.ru/users/imperituroard/']

    def parse(self, response):
        for url in response.css('#hubs_data_items > li a::attr("href")').re("*/hub/*"):
            yield scrapy.Request(response.urljoin('https://habrahabr.ru/', url), self.parse_hub)

    def parse_hub(self, response):
        for url in response.css('div.posts_list h1 a::attr("href")').re("*/blog/*"):
            yield scrapy.Request(response(url), self.parse_titles)

    def parse_titles(self, response):
        loader = XPathItemLoader(item=BlogCategory(), response=response)
        loader.add_css('date', 'div.published::text')
        loader.add_css('title', 'div.post_title::text')
        loader.add_css('article', 'div.content html_format::text')
        yield loader.load_item()
