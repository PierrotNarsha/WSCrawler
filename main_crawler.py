#112.164.99.250

from papago import Papago
from WsCrawler import WsCrawler
import json

card_no = 'WE35-45'

jp2ko = '◇' + 'ダ・カーポ＆Dal Segno ◇ 魔法・オモチャ ◇ よーし、がんばるぞ～！ ◇ 【起】【カウンター】 助太刀2000 レベル1 ' \
                        '[(1) 手札のこのカードを控え室に置く]（あなたは自分のフロントアタックされているキャラを1枚選び、そのターン中、' \
                        'パワーを+2000）'


if __name__ == '__main__':
    wc = WsCrawler()

    data = wc.read_CardData(card_no=card_no)
    print(data)

