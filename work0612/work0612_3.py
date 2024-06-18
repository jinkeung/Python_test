#웹사이트 크롤링[모든 정보 수집] 작업
#스크래핑[데이터 선별]

#정적 크롤링- 세션에 대한 동기화 필요X
import requests #웹페이지 요청
from bs4 import BeautifulSoup as bs

#동적 크롤링
import pyautogui
import selenium
import pandas as pd
import numpy as np

response=requests.get("https://www.ssg.com/sellerhome/154125/category.ssg?dispCtgId=6000208631&filterYn=Y&sellerViewType=seller-category&brandId=2000004090")
print(response)
print(response.status_code)
img=list()
name=list()
price=list()
if response.status_code==200:
    web=bs(response.text,'lxml')
    for i in web.find_all("img",class_="i1"):
        img.append(i.get("src"))
    for i in web.find_all("em",class_="tx_ko"):
        name.append(i.text)
    for i in web.find_all("em",class_="ssg_price"):
        price.append(i.text)

    new_name=list()
    for i in range(1,13,2):
        new_name.append(name[i])

    data=list()
    for i in range(len(img)):
        data.append(img[i])
        data.append(new_name[i])
        data.append(price[i])

    data=np.array(data).reshape(6,3)
    df=pd.DataFrame(data)
    df.to_excel("data.xlsx")