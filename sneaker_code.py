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
    sneakers = []
    try:
        with open(filename) as json_file:
            sneakers = json.load(json_file)
    except:
        sneakers = []
    return sneakers

def checkForRaffles(jsonFile):
    raffles = ([d for d in jsonFile if d['status'] == 'Enter Raffle'])
    return raffles

def saveFile(file, filename):
    with open(filename, 'w') as fout:
        json.dump(file, fout)

def checkForChanges():
    oldSneakerJson = getJSONFromFile('sneakers.json')
    if oldSneakerJson is []:
        oldSneakerJson = newCrawl('sneakers')

    newCrawl('sneakers_new')
    newSneakerJson = getJSONFromFile('sneakers_new.json')

    # print(newSneakerJson)
    difference = [x for x in newSneakerJson if x not in oldSneakerJson or x not in newSneakerJson]
    print("Length of old JSON: " + str(len(oldSneakerJson)))
    print("Length of new JSON: " + str(len(newSneakerJson)))
    print("Length of difference: " + str(len(difference)))
    print(difference)

    new_raffles = checkForRaffles(difference)
    live_raffles = checkForRaffles(newSneakerJson)

    changes = {"changes": False, "raffle": False, "live_raffle": False, "raffle-details": []}
    if difference:
        changes["changes"] = True
    if new_raffles:
        changes["raffle"] = True
        changes["raffle_details"] = difference
    if live_raffles:
        changes["live_raffle"] = True

    saveFile(newSneakerJson, "sneakers.json")
    #check for changes here
    # old sneakers = new sneakers
    # return {"changes": True, "raffle": False}
    return changes

def startup():
    # newCrawl('sneakers')
    print(checkForChanges())


# if __name__ == "__main__":
#     print(checkForChanges())