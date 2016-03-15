import scrapy
from scrapy.loader import ItemLoader
import json
import codecs
from scrapy.loader.processors import TakeFirst
from BeautifulSoup import BeautifulSoup


# class JsonWithEncodingPipeline(object):
#
#     def __init__(self):
#         self.file = codecs.open('scraped_data_utf8.json', 'w', encoding='utf-8')
#
#     def process_item(self, item, spider):
#         line = json.dumps(dict(item), ensure_ascii=False) + "\n"
#         self.file.write(line)
#         return item
#
#     def spider_closed(self, spider):
#         self.file.close()


class BlogCategory(scrapy.Item):
    # date = scrapy.Field()
    # title = scrapy.Field()
    article = scrapy.Field()


class BlogSpider(scrapy.Spider):
    name = 'hubrspider'
    start_urls = ['https://habrahabr.ru/users/imperituroard/']

    # custom_settings = {
    #     'ITEM_PIPELINES': {'hubrspider.JsonWithEncodingPipeline'}
    # }

    def parse(self, response):
        for url in response.css('#hubs_data_items > li a::attr("href")').re(".*/hub/.*"):
            yield scrapy.Request(response.urljoin(url), self.parse_page)

    def parse_page(self, response):
        for url in response.css('div.posts_list h1 a::attr("href")').re(".*/blog/.*"):
            yield scrapy.Request(response.urljoin(url), self.parse_titles)

        # Takes all pages of Hub
        # for url in response.css('#next_page::attr("href")').re(".*/page.*"):
        #     if url:
        #         yield scrapy.Request(response.urljoin(url), self.parse_page)

    def parse_titles(self, response):
        loader = ItemLoader(item=BlogCategory(), response=response)
        # loader = BeautifulSoup(item=BlogCategory(), response=response)
        # loader.append(self, 'div.post_title a::text')
        # loader.add_css('date', 'div.published::text')
        # loader.add_css('title', 'div.company_post h1 span::text')
        loader.add_css('article', 'div.content::text')
        yield loader.load_item()
