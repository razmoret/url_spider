from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://rarbg.to/torrents.php"

driver = webdriver.Chrome('../res/chromedriver')
driver.get(URL)
time.sleep(3)	# 停留五秒鐘

driver.find_element(By.ID, 'searchinput').send_keys('The Batman')	# 將 The Batman 輸入到搜尋框
time.sleep(2)	# 停留三秒鐘
driver.find_element(By.CLASS_NAME, 'btn').click()	# 點擊搜尋按鈕

time.sleep(2)	# 停留三秒鐘
driver.close()



