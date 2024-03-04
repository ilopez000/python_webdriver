import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# URL de Google
url = 'https://www.google.com'

# Inicializar el driver de Chrome
driver = webdriver.Chrome()

# Abrir la página de Google
driver.get(url)

# Esperar a que el cuadro de texto de búsqueda sea interactuable
search_box = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "APjFqb"))
)

# Escribir "hola" en el cuadro de texto de búsqueda
search_box.send_keys("hola")

# Encontrar el botón de búsqueda usando el nombre del botón y hacer clic en él
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "btnK"))
)
search_button.click()

# Esperar antes de cerrar (opcional, para ver los resultados)
time.sleep(2)

# Cerrar el navegador
driver.close()
