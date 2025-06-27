from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# --- Credenciais para o site de teste ---
USUARIO = "standard_user"
SENHA = "secret_sauce"

# --- Configuração do WebDriver ---
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.maximize_window()

try:
    # --- ETAPA 1: LOGIN ---
    print("--- Iniciando Etapa 1: Login ---")
    driver.get("https://www.saucedemo.com/")
    wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    driver.find_element(By.ID, "user-name").send_keys(USUARIO)
    driver.find_element(By.ID, "password").send_keys(SENHA)
    driver.find_element(By.ID, "login-button").click()
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))
    print("Login realizado com sucesso.")

    # --- ETAPA 2: ADICIONAR ITENS AO CARRINHO ---
    print("\n--- Iniciando Etapa 2: Adicionar Itens ao Carrinho ---")
    
    # Adiciona o primeiro item (mochila)
    # Usamos o seletor de atributo 'data-test', que é ótimo para automação
    driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-backpack"]').click()
    print("Item 'Sauce Labs Backpack' adicionado.")
    time.sleep(0.5) # Pausa para visualização

    # Adiciona o segundo item (luz de bicicleta)
    driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-bike-light"]').click()
    print("Item 'Sauce Labs Bike Light' adicionado.")

    # --- ETAPA 3: VERIFICAR O ÍCONE DO CARRINHO ---
    print("\n--- Iniciando Etapa 3: Verificar Ícone do Carrinho ---")
    
    # Encontra o número (badge) no ícone do carrinho
    badge_carrinho = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    
    # Verifica se o número de itens exibido é "2"
    if badge_carrinho.text == "2":
        print(f"✅ Verificação do ícone do carrinho: OK! Mostrando '{badge_carrinho.text}' itens.")
    else:
        print(f"❌ FALHA na verificação do ícone do carrinho! Mostrando '{badge_carrinho.text}', esperado '2'.")

    time.sleep(1)

    # --- ETAPA 4: IR PARA O CARRINHO E VERIFICAR OS ITENS ---
    print("\n--- Iniciando Etapa 4: Verificar Página do Carrinho ---")
    
    # Clica no ícone do carrinho para ir para a página de checkout
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    # Espera a página do carrinho carregar
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart_list")))
    print("Navegou para a página do carrinho.")

    # Pega o nome de todos os itens listados no carrinho
    itens_no_carrinho_elementos = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    # Extrai o texto de cada elemento e guarda numa lista
    nomes_itens_no_carrinho = [item.text for item in itens_no_carrinho_elementos]

    print(f"Itens encontrados no carrinho: {nomes_itens_no_carrinho}")

    # Lista dos itens que esperamos encontrar
    itens_esperados = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]

    # Verifica se a quantidade e os nomes dos itens estão corretos
    if len(nomes_itens_no_carrinho) == len(itens_esperados) and sorted(nomes_itens_no_carrinho) == sorted(itens_esperados):
        print("✅ Verificação final: OK! Os itens corretos estão no carrinho.")
    else:
        print("❌ FALHA na verificação final! Os itens no carrinho não correspondem ao esperado.")

    # --- SUCESSO GERAL ---
    print("\n===================================")
    print("🎉 Script de fluxo de compras executado com sucesso!")
    print("===================================")
    
    print("\nO navegador será fechado em 10 segundos...")
    time.sleep(10)

except Exception as e:
    print(f"\n❌ ERRO: Ocorreu um problema durante a execução do fluxo.")
    print(f"Detalhes do erro: {e}")
    driver.save_screenshot("erro_fluxo_compras.png")
    print("Uma imagem do erro foi salva como 'erro_fluxo_compras.png'")
    time.sleep(5)

finally:
    print("Fechando o navegador.")
    driver.quit()