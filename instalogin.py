import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

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

# Acesse a página de login do Instagram
driver.get("https://www.instagram.com/accounts/login/")

try:
    # Verifique se o elemento username existe
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    # Verifique se o elemento password existe
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )

    # Preencha o campo de usuário e senha
    username_field.send_keys("abra_paola")
    password_field.send_keys("Sey17zalel17@$")

    # Localize o botão de login
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1xmf6yo x1e56ztr x540dpk x1m39q7l x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"]/button'))
    )

    # Clique no botão de login
    login_button.click()

    print("Login realizado com sucesso!")

    # Espere até que o elemento SVG com aria-label="Direct" esteja presente na página
    direct_icon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//svg[@aria-label="Direct"]'))
    )

    print("Login bem-sucedido!")

except TimeoutException:
    print("Elementos de login não encontrados!")

finally:
    # Feche o navegador
    driver.quit()