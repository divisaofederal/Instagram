import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Configurações do Chrome Headless
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.100 Safari/537.36')
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--disable-web-security') 
chrome_options.add_argument('--allow-running-insecure-content')

# Inicializa o WebDriver
driver = webdriver.Chrome(options=chrome_options)

# URL do site a ser acessado
url = "https://help.instagram.com/"

# Configura a espera implícita para 10 segundos
driver.implicitly_wait(10)

try:
    # Acessa a URL
    driver.get(url)
    
    # Localiza o elemento pelo seletor CSS
    search_input = driver.find_element(By.CSS_SELECTOR, 'input._52ji._56bg._55wq._6il8')
    
    # Se o elemento estiver presente, imprime a mensagem de sucesso
    print("Página acessada com sucesso.")
    print("Elemento localizado:", search_input)
    
except Exception as e:
    # Em caso de erro, imprime a mensagem de falha
    print("Falha ao localizar o elemento:", e)

finally:
    # Fecha o navegador
    driver.quit()