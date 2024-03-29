import json

import requests as req
from bs4 import BeautifulSoup as bts


class Papago:

    # def __init__(self, card_data):
    def __init__(self):
        self.base_url = 'https://papago.naver.com/?sk=ja&tk=ko&hn=0&st='
        self.header = {

        }
        # self.data = card_data

    def send_req(self):
        jp2ko = '◇' + 'ダ・カーポ＆Dal Segno ◇ 魔法・オモチャ ◇ よーし、がんばるぞ～！ ◇ 【起】【カウンター】 助太刀2000 レベル1 ' \
                      '(1) ◈手札のこのカードを控え室に置く◈あなたは自分のフロントアタックされているキャラを1枚選び、そのターン中、' \
                      'パワーを+2000'

        # jp2ko = '\'ダ・カーポ＆Dal Segno | 魔法・オモチャ ◇ よーし、がんばるぞ～！ | 【起】【カウンター】 助太刀2000 レベル1 ' \
        #               '(1) 手札のこのカードを控え室に置く（あなたは自分のフロントアタックされているキャラを1枚選び、そのターン中、' \
        #               'パワーを+2000）\''

        send_url = self.base_url + jp2ko
        print(send_url)

        response = req.get(send_url)
        if response.status_code == 200:
            json_data = json.load(response.text)
            html = response.text
            soup = bts(html, 'html.parser')
            card = soup.find('div', id='txtTarget')

        return card
