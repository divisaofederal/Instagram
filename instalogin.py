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

# Acessar a página de login
driver.get("https://www.instagram.com/accounts/login/")

# Esperar até que o campo de nome de usuário esteja presente na página
username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']")))

# Inserir usuário com um atraso e movimento de mouse
for char in "seyzalel":
    username_input.send_keys(char)
    time.sleep(random.uniform(0.1, 0.3))
    ActionChains(driver).move_by_offset(random.uniform(1, 5), random.uniform(1, 5)).perform()

# Esperar um pouco antes de inserir a senha
time.sleep(random.uniform(1, 2))

# Inserir senha com um atraso e movimento de mouse
password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
for char in "Sey17zalel17@$":
    password_input.send_keys(char)
    time.sleep(random.uniform(0.1, 0.3))
    ActionChains(driver).move_by_offset(random.uniform(1, 5), random.uniform(1, 5)).perform()

# Esperar um pouco antes de clicar no botão de login
time.sleep(random.uniform(1, 2))

# Localizar e clicar no botão de login com um pequeno desvio no movimento do mouse
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
ActionChains(driver).move_to_element(login_button).perform()
time.sleep(random.uniform(0.5, 1))
login_button.click()

# Acessar a página do perfil específico
driver.get("https://www.instagram.com/abra_paola/")

# Esperar até que o ícone de opções esteja presente na página do perfil
try:
    options_icon = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "svg[aria-label='Opções']")))
    print("Acessou a página com sucesso.")
except:
    print("Erro: A página não foi carregada corretamente ou o elemento não está presente.")

# Aguardar um tempo aleatório antes de fechar o navegador
time.sleep(random.uniform(3, 5))

# Fechar o navegador
driver.quit()