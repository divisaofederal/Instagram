from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Substitua estas variáveis pelos seus dados de login
USERNAME = 'seyzalel'
PASSWORD = 'Sey17zalel17@$'

def login_instagram(username, password):
    # Opções do navegador
    options = Options()
    options.add_argument("--headless")  # Roda em modo headless
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # Define um user agent para simular uma versão recente de um navegador popular
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36")

    # Inicializa o driver do navegador com as opções definidas
    driver = webdriver.Chrome(options=options)

    # Acessa a página de login do Instagram diretamente
    driver.get("https://www.instagram.com/accounts/login/")

    # Aguarda para garantir que a página foi carregada
    time.sleep(5)

    # Encontra os campos de usuário e senha e os preenche
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")

    username_input.send_keys(username)
    time.sleep(2)
    password_input.send_keys(password)
    time.sleep(2)

    # Encontra e clica no botão de login
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    time.sleep(5)

    # Verifica se o login foi bem-sucedido
    current_url = driver.current_url
    if "accounts" in current_url and "onetap" in current_url:
        print("Login bem-sucedido!")
    else:
        print("Falha no login.")

    # Fecha o navegador
    driver.quit()

if __name__ == "__main__":
    login_instagram(USERNAME, PASSWORD)