import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url='https://www.google.com'

driver = webdriver.Chrome()
driver.get(url)
time.sleep(30000)

driver.close()
