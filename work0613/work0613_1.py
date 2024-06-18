from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://www.google.com")
driver.implicitly_wait(10)

driver.execute_script("window.open('https://www.naver.com')")
print(driver.window_handles)        #탭에대한 정보
print(driver.window_handles[0])
print(driver.window_handles[1])
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)
driver.switch_to.window(driver.window_handles[-1])      #-1번째(가장최신) 탭으로 이동(switch)
driver.execute_script("window.scrollTo(0,1000)")

#driver.switch_to.window()
time.sleep(5)

