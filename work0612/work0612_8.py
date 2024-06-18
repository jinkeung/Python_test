from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
op=webdriver.ChromeOptions()
op.add_argument('--start-maximized')
driver=webdriver.Chrome(options=op)
driver.get('https://www.naver.com')

driver.implicitly_wait(10)
'''
wait=WebDriverWait(driver, 10)
try:
    ele=wait.until(

        #EC.presence_of_element_located()
        #EC.visibility_of_element_located()
        #EC.element_to_be_selected()
        EC.element_to_be_clickable((By.TAG_NAME,"button"))
    )
except Exception:
    pass
ele.click()
time.sleep(5)
'''

search=driver.find_element(By.XPATH,'//*[@id="query"]')
webdriver.ActionChains(driver).move_to_element(search).send_keys("Hello").send_keys(Keys.ENTER)     #체이닝 작업으로 한번에 이어서 가능
time.sleep(5)