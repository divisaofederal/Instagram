from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Substitua estas variáveis pelos seus dados de login
USERNAME = 'abra_paola'
PASSWORD = 'Sey17zalel17@$'

def login_instagram(username, password):
    # Opções do navegador
    options = Options()
    options.add_argument("--headless")  # Roda em modo headless
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--ignore-certificate-errors")
    # Define um user agent para simular uma versão recente de um navegador popular
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36")

    # Inicializa o driver do navegador com as opções definidas
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1024, 768)

    # Acessa a página de login do Instagram diretamente
    driver.get("https://www.instagram.com/accounts/login/")

    # Use WebDriverWait para aguardar o elemento ser carregado
    username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))

    username_input.send_keys(username)
    # Introduce a random delay
    time.sleep(random.uniform(1, 3))
    password_input.send_keys(password)

    # Mais um atraso aleatório antes de clicar no login
    time.sleep(random.uniform(1, 3))
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_button.click()

    # Espera pela presença do botão "Agora não" e clica nele se estiver presente
    try:
        now_not_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@role='button'][contains(text(), 'Agora não')]")))
        now_not_button.click()
        print("Login bem-sucedido! E o clique em 'Agora não' foi bem sucedido.")
    except:
        print("Falha no login ou na ação pós-login.")

    # Fecha o navegador
    driver.quit()

if __name__ == "__main__":
    login_instagram(USERNAME, PASSWORD)