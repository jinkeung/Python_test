#웹사이트 크롤링[모든 정보 수집] 작업
#스크래핑[데이터 선별]

#정적 크롤링- 세션에 대한 동기화 필요X
import requests #웹페이지 요청
from bs4 import BeautifulSoup as bs

#동적 크롤링
import pyautogui
import selenium
import pandas as pd

response=requests.get("https://www.swagkey.kr/39",headers={"User-Agent":"Mozilla/5.0"})
print(response)
print(response.status_code)

if response.status_code == 200:
    web=bs(response.content,'lxml')

    '''
    for i in web.find_all("div",attrs={"class","shop-item"}):
        print(i.find(attrs={"class","_org_img"}).get("data-original"))
        print(i.find("h2").text.strip())
        print(i.find("p",attrs={"class","inline-blocked"}).text.strip())
    '''

    for num,i in enumerate(web.find_all("div",attrs={"class","shop-item"})):
        a=requests.get(i.find(attrs={"class","_org_img"}).get("data-original"))
        with open(str(num)+".jpg","wb")as file:
            file.write(a.content)
