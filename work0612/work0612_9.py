from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.keys import Keys
op=webdriver.ChromeOptions()
op.add_argument('--start-maximized')
driver=webdriver.Chrome(options=op)
driver.get('http://192.168.0.35:8081/')

search=driver.find_element(By.XPATH,'/html/body/form/input[1]')
button=driver.find_element(By.XPATH,'/html/body/form/input[3]')


webdriver.ActionChains(driver).move_to_element(search).click().send_keys("Hello World").send_keys(Keys.TAB).send_keys("1234").move_to_element(button).click().perform()

time.sleep(5)