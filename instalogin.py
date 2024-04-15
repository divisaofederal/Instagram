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
    # Movimento aleatório do mouse e scroll
    action = ActionChains(driver)
    start_element = driver.find_element(By.TAG_NAME, 'body')
    action.move_to_element(start_element).perform()
    time.sleep(random.uniform(1, 2))
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

    # Acessa a página de login do Instagram
    driver.get("https://www.instagram.com/accounts/login/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(password)

    simulate_human_behavior(driver)

    # Clica no botão de login e espera o login ser bem-sucedido
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
    time.sleep(random.uniform(5, 8))  # Espera pela navegação após o login
    
    print("Login bem-sucedido!")

    # Acessa a URL do perfil
    profile_url = "https://www.instagram.com/margaridagoncalves662?igsh=MXVmd2w0ZXNtczRveA=="
    driver.get(profile_url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))  # Garante que a página carregou
    
    # Clica no botão "Seguir"
    follow_button_xpath = "//div[contains(@class, 'x9f619')]"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, follow_button_xpath))).click()
    print("Clique em 'Seguir' realizado com sucesso.")

    # Fecha o navegador
    driver.quit()

if __name__ == "__main__":
    login_instagram(USERNAME, PASSWORD)