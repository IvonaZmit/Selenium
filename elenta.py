# pip install selenium
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("http://www.elenta.lt")
driver.find_element(By.XPATH, '//*[@id="header-container-nav"]/a[3]').click()
driver.find_element(By.XPATH,'//*[@id="form"]/fieldset/table/tbody/tr[8]/td[2]/p/a').click()
driver.find_element(By.ID, "Email").send_keys("qwert@gmail.com")
driver.find_element(By.ID, "Password").send_keys("qwerty")
driver.find_element(By.ID, "Password2").send_keys("qwerty")
time.sleep(4)
driver.find_element(By.XPATH, '//*[@id="form"]/fieldset/table/tbody/tr[8]/td[2]/input').click()

#ads_container = driver.find_element(By.CLASS_NAME,"")
#ads = ads_container.find_elements(By.CLASS_NAME,"")
#for ad in ads:
#    print(ad.text)
time.sleep(1000)

#driver.quit()
#driver.close()


