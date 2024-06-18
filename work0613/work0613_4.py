from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd

driver=webdriver.Chrome()
driver.get("https://www.swagkey.kr/41")
driver.implicitly_wait(10)

data=list()

for i in range(0,6):
    data.append([])
    for j in range(2):
        data[i].append(0)


for num,i in enumerate(driver.find_elements(By.CLASS_NAME,"item-wrap")):
    link=(i.find_element(By.TAG_NAME,"A").get_attribute("href"))
    driver.switch_to.new_window()
    driver.get(link)
    data[num][0]=driver.find_element(By.CLASS_NAME,"view_tit").text
    data[num][1]=driver.find_element(By.CLASS_NAME,"goods_summary").text
    driver.close()
    driver.switch_to.window(driver.window_handles[0])





data=pd.DataFrame(data,columns=['name','text'])
data.to_excel("keyboard2.xlsx")



time.sleep(3)