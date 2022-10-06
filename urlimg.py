import json
import urllib.request as url_req
import requests
from bs4 import BeautifulSoup as bts
import time
import os

max_val = 99
cnt = 0

directory_name = "DownLoad Image"

url = "https://story.kakao.com/1probl/I7eTlFyj84a/photos/"

if __name__ == '__main__':

    while True:

        url = input("URL : ")

        # max_val = int(input("Max Value : "))

        directory_name = input("폴더 명 : ")

        if url == "":
            continue
        if directory_name == "":
            continue

        try:
            os.mkdir(directory_name)
        except:
            print("저장 폴더를 생성할 수 없습니다.")
            print("이름이 같은 폴더가 있는 경우, 해당 폴더에 저장됩니다.")

        try:
            req = requests.get(url + str(cnt))

            text = bts(req.text, 'html.parser')

            top = text.select('script')

            # text = urllib.urlopen(url+str(cnt))

            boot = top[1]
            mid = str(boot)
        except:
            print("Not Found URL!!")
            continue

        while cnt <= max_val:
            try:
                img_url = mid[mid.find("https"): mid.find("thumbnail_url2")-3]

                # print(img_url)

                url_req.urlretrieve(img_url, os.getcwd() + "/" + directory_name + "/" + str(cnt) + ".jpg")

                cnt = cnt + 1

                # print(mid.find("searchable"))

                mid = mid[mid.find("searchable")+10:]
            except:
                print("Success!")
                break

        # input("종료를 하실려면 아무키나 입력해 주세요")
