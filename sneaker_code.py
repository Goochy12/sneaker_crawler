# import scrapy
# from scrapy.crawler import CrawlerProcess
# from sneaker_crawler.spiders import raffles
#
# if __name__ == "__main__":
#     process = CrawlerProcess()
#     process.crawl(raffles.RafflesSpider)
#     process.start()

import os
import json

def newCrawl(filename):
    os.system(f'scrapy crawl raffles -O {filename}.json')

def getJSONFromFile(filename):
    sneakers = {}
    with open(filename) as json_file:
        try:
            sneakers = json.load(json_file)
        except:
            sneakers = {}
    return sneakers

def checkForRaffles():
    oldSneakerJson = getJSONFromFile('sneakers.json')
    return ([d for d in oldSneakerJson if d['status'] == 'Enter Raffle'])

def checkForChanges():
    oldSneakerJson = getJSONFromFile('sneakers.json')
    if oldSneakerJson is {}:
        newCrawl('sneakers')

    newCrawl('sneakers_new')
    newSneakerJson = getJSONFromFile('sneakers_new.json')

    #check for changes here
    # old sneakers = new sneakers
    return

def startup():
    newCrawl('sneakers')

