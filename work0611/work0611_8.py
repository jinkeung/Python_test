from selenium import webdriver
#동적 크롤링
from bs4 import BeautifulSoup as bs
#정적 크롤링

import pyautogui as gui
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
#driver.implicitly_wait(100)  #암묵적 (wait)
#WebDriverWait(driver,100)    #명시적
driver.implicitly_wait(10)



driver.get("https://www.naver.com")
driver.maximize_window()
driver.find_element(By.XPATH,'//*[@id="account"]/div/a').click()
driver.find_element(By.XPATH,'//*[@id="qrcode"]').click()
time.sleep(15)
nick=driver.find_element(By.XPATH,'//*[@id="account"]/div[1]/div/div/div[1]/a[1]/span')
print(nick.text)
id=driver.find_element(By.XPATH,'//*[@id="account"]/div[1]/div/div/div[2]')
print(id.text)





