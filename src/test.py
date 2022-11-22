



URL = "https://rarbg.to/torrents.php"
URL ='https://www.google.com.tw'
URL = 'https://movies.yahoo.com.tw/'	# Yahoo 電影網站的網址


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('../res/chromedriver')

driver.get(URL)
time.sleep(3)	# 停留五秒鐘
"""
driver.find_element_by_id('serchinput').send_keys('The Batman')	# 將 The Batman 輸入到搜尋框
time.sleep(3)	# 停留三秒鐘
driver.find_element_by_xpath('//*[@id="y_serch_l"]/form/button[1]').click()	# 點擊搜尋按鈕
"""

driver.find_element(By.ID, 'serchinput').send_keys('The Batman')	# 將 The Batman 輸入到搜尋框
time.sleep(2)	# 停留三秒鐘
driver.find_element(By.CLASS_NAME, 'serch_movie').click()	# 點擊搜尋按鈕

time.sleep(2)	# 停留三秒鐘
driver.close()



