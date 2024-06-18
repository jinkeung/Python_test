import requests     #pip install requests
#웹페이지 요청[마크업언어의 데이터 요청[태그, 속성, 속성값]]
import bs4    #pip install beautifulsoup
from bs4 import BeautifulSoup
#웹페이지 파싱 역할(파싱? : 변환해서 대입) <- 웹페이지 정보
        # + 선택자 . . .


response=requests.get('https://news.naver.com/')
print(response) # [200]: 웹페이지와의 연결 완료

if response.status_code == 200:        # 안전장치(try catch느낌)
    web=BeautifulSoup(response.text,'lxml') #목적에 따른 parser 사용
    print(web.find("a"))         #find: 첫번째태그
    print(web.find_all("a"))     #find_all: 모든 a태그[리스트형태]
    for i in web.find_all("a"):
        print(i.get_text())
    print(web.select("div> button"))   #select 선택자(class, id, 복합 . . .)

    for i in web.find_all("div",class_="news_info"):
        print(i.get_text())
    for i in web.find_all("div",attrs={"class":"news_info"}):
        print(i.get_text())

