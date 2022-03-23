#112.164.99.250

from WsCrawler import WsCrawler
import json

card_no = 'WE36-44'

if __name__ == '__main__':
    wc = WsCrawler()

    data = wc.read_CardData(title_code='HOL', card_no=card_no)
    print(data)

