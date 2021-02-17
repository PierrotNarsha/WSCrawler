#112.164.99.250

import requests as req
from bs4 import BeautifulSoup as bts
import json

url = "https://ws-tcg.com/cardlist/?cardno=DC/W01-002"

papago = "https://papago.naver.com/?sk=ja&tk=ko&hn=0&st="

def read_CardData():
    response = req.get(url)

    data = json

    if response.status_code == 200:

        html = response.text
        soup = bts(html, 'html.parser')
        card = soup.find(id='cardDetail').find("tbody")

        # first = card.find_next()
        # card_name = first.find_next('img')['alt']
        # card_img_url = first.find_next('img')['src']

        tr_count = len(card.find_all('tr'))

        cnt1, cnt2, cnt3, = 0, 0, 0

        for tr in card.find_all('tr'):
            #if tr['class'] is 'first':
            #   print(tr.find_next('img')['src'])
            th_count = len(tr.find_all('th'))
            td_count = len(tr.find_all('td'))

            if th_count is 1 and td_count is 1:
                cnt1 += 1
                if tr.find('th') is 'カード番号':

                elif tr.find('th') is '商品名':
                elif tr.find('th') is 'ネオスタンダード区分':
                elif tr.find('th') is '特徴':
                elif tr.find('th') is 'テキスト':
                elif tr.find('th') is 'フレーバー':

            elif th_count is 2 and td_count is 2:
                cnt2 += 1

                th_all = tr.find_all('th')
                td_all = tr.find_all('td')




            elif th_count is 1 and td_count is 2:
                cnt3 += 1
                card_img_url = tr.find('img')['src']
                card_name = tr.find_all('td')[1].get_text()

        if cnt1 + cnt2 + cnt3 is tr_count:
            print('true')
        else:
            print('false')

if __name__ == '__main__':
    read_CardData()
