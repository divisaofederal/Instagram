import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

# Acessar a página específica do Help Center do Instagram
driver.get("https://help.instagram.com/contact/723586364339719")

# Esperar até que o título da página contenha "Central de Ajuda do Instagram"
WebDriverWait(driver, 10).until(EC.title_contains("Central de Ajuda do Instagram"))

# Verificar se o título da página contém "Central de Ajuda do Instagram"
if "Central de Ajuda do Instagram" in driver.title:
    print("Acessou a página com sucesso.")
else:
    print("Erro: O título da página não contém 'Central de Ajuda do Instagram'.")

# Fechar o navegador
driver.quit()