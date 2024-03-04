import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver_path = 'C:\\Users\\ignac\\PycharmProjects\\pythonProject13\\chromedriver.exe'  # Actualiza esto con la ruta correcta
driver = webdriver.Chrome(executable_path=driver_path)
url='www.google.com'

driver = webdriver.Chrome()
driver.get(url)


driver.close()
