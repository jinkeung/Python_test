from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://www.google.com")
driver.implicitly_wait(10)
print(driver.current_url)

driver.switch_to.new_window()
driver.get("https://naver.com")
driver.execute_script("scrollTo(0,500)")
print(driver.current_url)

time.sleep(3)
