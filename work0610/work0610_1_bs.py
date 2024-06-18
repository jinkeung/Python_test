#정적크롤링[모든데이터 긁어오기]

import requests
#Server 정보 요청[Get]-HTML
from bs4 import BeautifulSoup as bs
#HTML, XML 파싱
import tkinter as tk


def news_title():
    response=requests.get("https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=%EB%84%B7%EB%A7%88%EB%B8%94")
    #print(response)        #200

    if response.status_code==200:
        web=bs(response.text,"lxml")    #C언어로 구현
        data=web.find_all("a",{"class":"news_tit"})
        data_title=list()
        for i in data:
            data_title.append(i.get_text())
    print(data_title)

    return data_title