#웹사이트 크롤링[모든 정보 수집] 작업
    #스크래핑[데이터 선별]

#정적 크롤링- 세션에 대한 동기화 필요X
import requests #웹페이지 요청
from bs4 import BeautifulSoup as bs

#동적 크롤링
import pyautogui
import selenium

response=requests.get("https://lgonlinestore.co.kr/category/%EB%A1%9C%EC%A7%80%ED%85%8Dg/66/")
print(response)
print(response.status_code)

print(response.text)