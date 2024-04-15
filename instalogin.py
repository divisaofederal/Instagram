from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Substitua estas variáveis pelos seus dados de login
USERNAME = 'testeseyza28'
PASSWORD = 'testeseyza28@$'

def simulate_human_behavior(driver):
    """
    Simula comportamentos humanos básicos para reduzir as chances de detecção.
    """
    # Movimento aleatório do mouse
    action = ActionChains(driver)
    start_element = driver.find_element(By.TAG_NAME, 'body')
    action.move_to_element(start_element).perform()
    time.sleep(random.uniform(1, 2))
    
    # Scroll aleatório na página
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4);")
    time.sleep(random.uniform(1, 2))
    driver.execute_script("window.scrollTo(0, -document.body.scrollHeight/4);")

def login_instagram(username, password):
    # Opções do navegador
    options = Options()
    options.add_argument("--headless")  # Roda em modo headless
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36")
    
    # Inicializa o driver do navegador com as opções definidas
    driver = webdriver.Chrome(options=options)

    # Acessa a página de login do Instagram diretamente
    driver.get("https://www.instagram.com/accounts/login/")

    # Aguarda até que os campos de login estejam presentes
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))

    simulate_human_behavior(driver)

    # Encontra os campos de usuário e senha e os preenche
    driver.find_element(By.NAME, "username").send_keys(username)
    time.sleep(random.uniform(2, 4))
    driver.find_element(By.NAME, "password").send_keys(password)

    simulate_human_behavior(driver)

    # Clicar no botão de login
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    action = ActionChains(driver)
    action.move_to_element(login_button).click().perform()

    # Espera por uma navegação ou por um tempo limite para considerar o login bem-sucedido
    time.sleep(random.uniform(5, 8))
    
    print("Login bem-sucedido!")

    # Fecha o navegador
    driver.quit()

if __name__ == "__main__":
    login_instagram(USERNAME, PASSWORD)