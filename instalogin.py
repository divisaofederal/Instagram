# All rights reserved to Seyzalel. Reproduction in whole or in part without prior permission is prohibited. © Seyzalel 2024

import time
import random
from selenium.common.exceptions import TimeoutException
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

try:
  driver.get("https://instagram.com/")
  entrar = WebDriverWait(driver, 10).until(
    
    EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "Entrar")]'))
  )
  entrar.click()
  
  input_username = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//input[@name="username"]'))
  )
  if input_username:
    print("O botão foi clicado com sucesso e o input foi encontrado.")
  else:
    print("Falha ao clicar no botão ou o input não foi encontrado.")
    
except TimeoutException:
  print("Tempo limite excedido ao aguardar o botão ou o input.")

except Exception as e:
  print("Ocorreu um erro:", e)

finally:
  driver.quit()