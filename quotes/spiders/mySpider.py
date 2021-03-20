import scrapy

from quotes.items import QuotesItem

class MyQuotes_Spider(scrapy.Spider):
    name = 'FirstSpider'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        quote_list = response.xpath('//div[@class= "quote"]')
        item = QuotesItem()
        for quote in quote_list:
            item['quote'] = quote.xpath('.//span[@class = "text"]/text()').get()
            item['author'] = quote.xpath('.//span/small[@class = "author"]/text()').get()
            item['tag'] = quote.xpath('.//div[@class = "tags"]/a/text()').getall()
            if item['tag'] == []:
                item['tag'] = ['no_tag']
            yield item
        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)



