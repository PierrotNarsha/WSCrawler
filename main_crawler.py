#112.164.99.250

from WsCrawler import WsCrawler
from pymongo import MongoClient
import json

# client = MongoClient("mongodb://")

title_code = 'SW'
pack_no = ['s49']

if __name__ == '__main__':
    wc = WsCrawler()

    for pack_index in range(0, len(pack_no)):
        data = wc.read_CardData(title_code=title_code, pack_no=pack_no[0])
        print(data)

