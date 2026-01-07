# pip install selenium
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("http://www.elenta.lt")
driver.find_element(By.ID, 'submit-new-ad-nav-button').click()
driver.find_element(By.XPATH,'//*[@id="select-top-category-list"]/li[6]/a').click()
driver.find_element(By.XPATH,'//*[@id="select-sub-category-list"]/li[2]/a').click()
driver.find_element(By.ID,"title").send_keys("DELL kompiuteris")
driver.find_element(By.ID,"text").send_keys("Naujas nenaudotas kompiuteris")
driver.find_element(By.ID,"price").send_keys("550")
driver.find_element(By.ID,"location-search-box").send_keys("Vilnius")
driver.find_element(By.ID,"phone").send_keys("+37065844966")
driver.find_element(By.ID,"email").send_keys("qwerty@gmail.com")
time.sleep(4)
btn = driver.find_element(By.ID,'submit-button')
ActionChains(driver).move_to_element(btn).perform()
time.sleep(3)
btn.click()
#driver.find_element(By.ID,"submit-button").click()
time.sleep(3)
#driver.quit()
#driver.close()