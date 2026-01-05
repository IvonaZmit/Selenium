# pip install selenium
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("http://www.elenta.lt")
driver.find_element(By.ID, "submit-new-ad-nav-button").click()
driver.find_element(By.XPATH,'//*[@id=""]').click()
driver.find_element(By.ID, "").send_keys("")
driver.find_element(By.ID,"").send_keys("")
driver.find_element(By.ID, "").send_keys("")
driver.find_element(By.ID, "").send_keys("")
driver.find_element(By.ID, "").send_keys("")
ads_container = driver.find_element(By.CLASS_NAME,"")
ads = ads_container.find_elements(By.CLASS_NAME,"")
for ad in ads:
    print(ad.text)
time.sleep(1000)



