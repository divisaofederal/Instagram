import time
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurações do Chrome
chrome_options = Options()
chrome_options.add_argument('--headless')  # Execução sem interface gráfica (headless)
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

# Inicializa o WebDriver do Chrome
driver = webdriver.Chrome(options=chrome_options)

try:
    # Abre a página de login do Instagram
    driver.get("https://www.instagram.com/accounts/login/")

    # Verifica se o título da página contém "Entrar"
    WebDriverWait(driver, 10).until(
        EC.title_contains("Entrar")
    )
    print("Página de login acessada com sucesso.")

    # Preenche o campo de username
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, 'username'))
    )
    username_input.send_keys("abra_paola")  # Substitua 'seu_usuario' pelo seu nome de usuário

    # Preenche o campo de senha
    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, 'password'))
    )
    password_input.send_keys("Sey17zalel17@$")  # Substitua 'sua_senha' pela sua senha

    # Clica no botão de login
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
    )
    login_button.click()

    # Aguarda até que a página seja carregada (título não contém "Entrar")
    WebDriverWait(driver, 10).until_not(
        EC.title_contains("Entrar")
    )
    
    # Verifica se o título da página contém apenas "Instagram"
    if "Instagram" in driver.title and not "Entrar" in driver.title:
        print("Login realizado com sucesso.")
    else:
        raise Exception("Erro ao realizar o login.")

    # Aguarda 7 segundos antes de fechar o navegador
    time.sleep(7)

except Exception as e:
    print("Ocorreu um erro:", e)

finally:
    # Fecha o navegador ao finalizar
    driver.quit()