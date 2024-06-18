import selenium
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://finance.naver.com/sise/lastsearch2.naver")
driver.maximize_window()

title=driver.find_elements(By.CLASS_NAME, "tltle")
for i in title:
    print(i.text)