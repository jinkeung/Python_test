from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd

driver=webdriver.Chrome()
driver.get("https://www.swagkey.kr/41")
driver.implicitly_wait(10)

links=list()
for i in driver.find_elements(By.CLASS_NAME,"item-wrap"):
    links.append(i.find_element(By.TAG_NAME,"A").get_attribute("href"))

data=list()

for i in range(0,len(links)):
    data.append([])
    for j in range(2):
        data[i].append(0)

for num,i in enumerate(links):
    driver.switch_to.new_window()
    driver.get(i)
    data[num][0]=driver.find_element(By.CLASS_NAME,"view_tit").text
    data[num][1]=driver.find_element(By.CLASS_NAME,"goods_summary").text

data=pd.DataFrame(data,columns=['name','text'])
data.to_excel("keyboard.xlsx")



time.sleep(3)