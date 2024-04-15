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

try:
    # Carregar a página
    driver.get("https://help.instagram.com/")

    # Esperar até que o elemento seja localizado
    search_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-label="Pesquisar na Central de Ajuda"]'))
    )

    # Se o elemento for encontrado, imprime a mensagem
    print("Página acessada com sucesso.")

finally:
    # Fechar o navegador
    driver.quit()