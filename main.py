import scrapy
from scrapy.crawler import CrawlerProcess
from sneaker_crawler.spiders import raffles

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(raffles)
    process.start()