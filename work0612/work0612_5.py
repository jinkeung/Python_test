#웹사이트 크롤링[모든 정보 수집] 작업
#스크래핑[데이터 선별]

#정적 크롤링- 세션에 대한 동기화 필요X
import requests #웹페이지 요청
from bs4 import BeautifulSoup as bs

#동적 크롤링
import pyautogui as gui
#import selenium
#requests +bs4
import cv2

#print(gui.locateOnScreen("sc.png",confidence=0.5))      #정확도 설정 가능
#gui.click(gui.locateOnScreen("sc.png",confidence=0.5))

from selenium import webdriver as web
import time
from selenium.webdriver.chrome.options import Options

op=Options()
op.add_argument('--start-maximized')

driver=web.Chrome(options=op)
driver.get("https://www.naver.com")
time.sleep(2)
print(gui.locateCenterOnScreen("naver_login.png",confidence=0.7))
gui.click(gui.locateCenterOnScreen("naver_login.png",confidence=0.7))

id=gui.prompt("아이디 입력","ID")
pw=gui.password("패스워드 입력","PW")
gui.write(id)
time.sleep(1)
gui.press("tab")
gui.write(pw)
time.sleep(1)
gui.press("enter")
gui.alert("BODY","TITLE")
a=gui.confirm("data","title",["ok","no"])
print(a)
time.sleep(5)

