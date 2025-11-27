
# pip install selenium
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("http://www.skelbiu.lt")
driver.find_element(By.XPATH,'//*[@id="onetrust-accept-btn-handler"]').click()
driver.find_element(By.ID, "searchKeyword").send_keys("kaledines dovanos")
driver.find_element(By.ID,"searchButton").click()
ads_container = driver.find_element(By.CLASS_NAME,"standard-list-container")
ads = ads_container.find_elements(By.CLASS_NAME,"title")
for ad in ads:
    print(ad.text)
time.sleep(1000)