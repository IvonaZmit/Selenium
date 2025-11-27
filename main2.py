+19
-7
Lines changed: 19 additions & 7 deletions
Original file line number	Diff line number	Diff line change
@@ -9,10 +9,22 @@
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
search_word = "eteriniai%20aliejai"
urls = []
for i in range(1,201):
    url_to_go = f'https://www.skelbiu.lt/skelbimai/{i}?keywords={search_word}'
    driver.get(url_to_go)
    print(driver.current_url)
    print(url_to_go)
    if driver.current_url != url_to_go:
        break
    ads_container = driver.find_element(By.CLASS_NAME,"standard-list-container")
    ads = ads_container.find_elements(By.TAG_NAME,"a")
    for ad in ads:
        url = ad.get_attribute("href")
        print(url)
        if "https://www.skelbiu.lt/skelbimai" in url:
            urls.append(url)
for url in urls:
    driver.get(url)
time.sleep(1000)
