from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

op=webdriver.ChromeOptions()
op.add_argument('--start-maximized')
driver=webdriver.Chrome(options=op)
driver.implicitly_wait(10)
driver.get('https://www.swagkey.kr/39')

for i in range(1,10):
    driver.find_element(By.XPATH,'//*[@id="container_w202406097eb40c015dfa1"]/div['+str(i)+']/div[1]/a/div').click()
    print(driver.find_element(By.CLASS_NAME,"view_tit").text)
    driver.back()
