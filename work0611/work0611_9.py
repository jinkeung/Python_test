from selenium import webdriver
#동적 크롤링

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

driver=webdriver.Chrome()
driver.get("https://www.naver.com")
driver.find_element(By.XPATH,'//*[@id="query"]').send_keys("오늘의 날씨")
driver.find_element(By.XPATH,'//*[@id="query"]').send_keys(Keys.ENTER)
driver.find_element(By.XPATH,'//*[@id="lnb"]/div[1]/div/div[1]/div/div[2]/div[2]/a/span').click()
driver.find_element(By.XPATH,'//*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[8]').click()
data=driver.find_elements(By.CLASS_NAME,'news_tit')


titles=list()
for i in data:
    titles.append(i.text)

titles=pd.Series(titles)
titles.to_excel("NEWS_TITLE.xlsx")

