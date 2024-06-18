from selenium import webdriver
#동적 크롤링
from bs4 import BeautifulSoup as bs
#정적 크롤링

import pyautogui as gui
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#op=Options()
#op.add_argument('headless')        #창을 안띄우고 구현

#driver=webdriver.Chrome(options=op)      #크롬실행, 옵션 조절

driver=webdriver.Chrome()
driver.get("https://naver.com")
driver.maximize_window()
'''
a=driver.find_elements(By.CLASS_NAME, "service_name")
time.sleep(2)
print(a)
for i in a:
    print(i.text)
b=driver.find_elements(By.TAG_NAME, "p")
for i in b:
    print(i.text)
'''
driver.find_element(By.XPATH,'//*[@id="account"]/div/a').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="id"]').send_keys("jinkeung")

time.sleep(5)


