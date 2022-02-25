import scrapy

class RafflesSpider(scrapy.Spider):
    name = "raffles"

    start_urls = [
        "https://www.supplystore.com.au/raffles.aspx",
    ]

    def parse(self, response):
        for sneaker in response.xpath('//div[has-class("post-row")]'):
            yield {
                'name' : sneaker.xpath('.//div[has-class("post-title-wrap")]//h3//a/text()').get(),
                'status': sneaker.xpath('.//div[has-class("post-link-wrap")]//h3//a/text()').get(),
            }