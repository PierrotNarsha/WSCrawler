import requests as req
from bs4 import BeautifulSoup as bts


class WsCrawler:

    def __init__(self):
        self.base_url = 'https://ws-tcg.com/cardlist/?cardno={0}/{1}'
        self.data = {'img_url': '',
                'card_name': '',
                'card_no': '',
                'pd_name': '',
                'neo': '',
                'title_no': '',
                'r': '',
                'side': '',
                'kind': '',
                'color': '',
                'level': '',
                'cost': '',
                'power': '',
                'soul': '',
                'trigger': '',
                'char': '',
                'ability': '',
                'dialogue': ''}

    def read_CardData(self, title_code, card_no):
        response = req.get(str.format(self.base_url, title_code, card_no))

        tmp_data = self.data

        if response.status_code == 200:

            html = response.text
            soup = bts(html, 'html.parser')
            card = soup.find(id='cardDetail').find('tbody')

            tr_count = len(card.find_all('tr'))

            cnt1, cnt2, cnt3, = 0, 0, 0

            trs = card.find_all('tr')

            for tr in trs:
                # if tr['class'] is 'first':
                #   print(tr.find_next('img')['src'])
                th_count = len(tr.find_all('th'))
                td_count = len(tr.find_all('td'))

                if th_count == 1 and td_count == 1:
                    cnt1 += 1

                    if tr.find('th').get_text() == 'カード番号':
                        tmp_data['card_no'] = tr.find('td').get_text()
                    elif tr.find('th').get_text() == '商品名':
                        tmp_data['pd_name'] = tr.find('td').get_text()
                    elif tr.find('th').get_text() == 'ネオスタンダード区分':
                        tmp_data['neo'] = tr.find('td').get_text()
                    elif tr.find('th').get_text() == '特徴':
                        tmp_data['char'] = tr.find('td').get_text()
                    elif tr.find('th').get_text() == 'テキスト':
                        tmp_data['ability'] = tr.find('td').get_text()
                    elif tr.find('th').get_text() == 'フレーバー':
                        tmp_data['dialogue'] = tr.find('td').get_text()

                elif th_count == 2 and td_count == 2:
                    cnt2 += 1

                    th_all = tr.find_all('th')
                    td_all = tr.find_all('td')

                    if th_all[0].get_text() == '作品番号':
                        tmp_data['title_no'] = td_all[0].get_text()
                    elif th_all[0].get_text() == 'サイド':
                        side = td_all[0].find('img')['src'][-5:-4]
                        if side == 'w':
                            tmp_data['side'] = 'ヴァイスサイド'
                        else:
                            tmp_data['side'] = 'シュヴァルツサイド'
                    elif th_all[0].get_text() == '色':
                        color = td_all[0].find('img')['src'][50:-4]
                        if color == 'yellow':
                            tmp_data['color'] = '黄'
                        elif color == 'green':
                            tmp_data['color'] = '緑'
                        elif color == 'red':
                            tmp_data['color'] = '赤'
                        elif color == 'blue':
                            tmp_data['color'] = '青'
                    elif th_all[0].get_text() == 'コスト':
                        tmp_data['cost'] = td_all[0].get_text()
                    elif th_all[0].get_text() == 'ソウル':
                        tmp_data['soul'] = len(td_all[0].find_all('img'))
                    if th_all[1].get_text() == 'レアリティ':
                        tmp_data['r'] = td_all[1].get_text()
                    elif th_all[1].get_text() == '種類':
                        tmp_data['kind'] = td_all[1].get_text()
                    elif th_all[1].get_text() == 'レベル':
                        tmp_data['level'] = td_all[1].get_text()
                    elif th_all[1].get_text() == 'パワー':
                        tmp_data['power'] = td_all[1].get_text()
                    elif th_all[1].get_text() == 'トリガー':
                        imgs = td_all[1].find_all('img')

                        if len(imgs) == 1:
                            tmp_data['trigger'] = imgs[0]['src'][50:-4]
                        elif imgs == []:
                            tmp_data['trigger'] = '-'
                        else:
                            tmp_data['trigger'] = imgs[0]['src'][50:-4] + "," + imgs[1]['src'][50:-4]

                elif th_count == 1 and td_count == 2:
                    cnt3 += 1
                    tmp_data['img_url'] = tr.find('img')['src']
                    tmp_data['card_name'] = tr.find_all('td')[1].get_text()

            self.data = tmp_data

            return self.data
