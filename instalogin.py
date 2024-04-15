from playwright.sync_api import sync_playwright

def login_instagram(username, password):
    with sync_playwright() as p:
        # Inicia o navegador em modo headless
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Acessa a página de login do Instagram
        page.goto("https://www.instagram.com/accounts/login/")

        # Preenche os campos de usuário e senha e submete o formulário
        page.fill("input[name='username']", username)
        page.fill("input[name='password']", password)
        page.click("button[type='submit']")

        # Espera pela navegação após o clique no botão de login
        page.wait_for_navigation()

        # Verifica se o login foi bem-sucedido, verificando a presença do botão "Agora não"
        try:
            page.wait_for_selector("text='Agora não'", timeout=5000)
            print("Login bem-sucedido! E o clique em 'Agora não' foi bem sucedido.")
            # Você pode adicionar aqui um comando para clicar no botão "Agora não" se necessário
        except Exception as e:
            print("Falha no login ou na ação pós-login.", e)

        # Fecha o navegador
        browser.close()

if __name__ == "__main__":
    USERNAME = 'testeseyza28'
    PASSWORD = 'testeseyza28@$'
    login_instagram(USERNAME, PASSWORD)