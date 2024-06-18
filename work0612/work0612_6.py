from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

op=Options()
op.add_argument('--start-maximized')
driver=webdriver.Chrome(options=op)
driver.get("https://www.swagkey.kr/39")
time.sleep(1)

img=driver.find_elements(By.CLASS_NAME,"shop-item")
for i in img:
    print(i.find_element(By.CLASS_NAME,"_org_img").get_attribute("data-original"))
driver.find_element(By.XPATH,'//*[@id="container_w202406097eb40c015dfa1"]/div[1]/div[1]/a').click()
time.sleep(2)
