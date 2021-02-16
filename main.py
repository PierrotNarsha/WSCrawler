#112.164.99.250

import requests as req
from bs4 import BeautifulSoup as bts
import json

url = "https://ws-tcg.com/cardlist/?cardno=DC/W01-002"

papago = "https://papago.naver.com/?sk=ja&tk=ko&hn=0&st="

def read_CardData():
    response = req.get(url)

    if response.status_code == 200:

        html = response.text
        soup = bts(html, 'html.parser')
        card = soup.find(id='cardDetail').find("tbody")

        first = card.find_next()
        card_name = first.find_next('img')['alt']
        card_img_url = first.find_next('img')['src']

        for th in card.find_all('th'):
            print(th)

        for td in card.find_all('td'):
            print(td)

        for tr in card.find_all('tr'):
            print(tr)

if __name__ == '__main__':
    read_CardData()
