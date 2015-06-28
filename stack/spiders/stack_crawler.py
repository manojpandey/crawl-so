import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from stack.items import StackItem


class StackCrawlerSpider(CrawlSpider):
    name = 'stack_crawler'
    allowed_domains = ['stackoverflow.com']

    # start_urls = ['http://www.stackoverflow.com/']
    start_urls = ['http://stackoverflow.com/questions?pagesize=50&sort=votes']
    
    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )

    rules = [
        Rule(LinkExtractor(allow=r'questions\?page=[0-9]&sort=votes'), callback='parse_item', follow=True)
    ]

    def parse_item(self, response):
        questions = response.xpath('//div[@class="summary"]/h3')

        for question in questions:
            item = StackItem()
            item['url'] = question.xpath(
                'a[@class="question-hyperlink"]/@href').extract()[0]
            item['title'] = question.xpath(
                'a[@class="question-hyperlink"]/text()').extract()[0]
            yield item