import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--disable-web-security') 
chrome_options.add_argument('--allow-running-insecure-content')

driver = webdriver.Chrome(options=chrome_options)

# Acessa a página de login do Instagram
driver.get("https://www.instagram.com/accounts/login/")

try:
  # Verifica se o elemento username existe
  username_field = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.NAME, "username"))
  )
  # Verifica se o elemento password existe
  password_field = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.NAME, "password"))
  )

  # Imprime mensagem de sucesso
  print("Página acessada com sucesso!")

except TimeoutException:
  print("Elementos de login não encontrados!")

finally:
  # Fecha o navegador
  driver.quit()