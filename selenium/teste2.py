from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- Configuração do Driver ---
driver = webdriver.Chrome()
# Define uma espera máxima de 10 segundos para todas as operações
wait = WebDriverWait(driver, 10)

# --- Ações no Navegador ---
try:
    # Abre a página
    driver.get("http://quotes.toscrape.com/")

    # Espera ATÉ que o primeiro elemento com a classe 'quote' esteja visível
    print("Aguardando o conteúdo carregar...")
    primeira_citacao = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "quote")))

    # Agora que garantimos que carregou, podemos interagir
    print("Conteúdo carregado! Extraindo a primeira citação.")

    # Extrai o texto da citação e o autor
    texto_citacao = primeira_citacao.find_element(By.CLASS_NAME, "text").text
    autor_citacao = primeira_citacao.find_element(By.CLASS_NAME, "author").text

    print("\n--- CITAÇÃO ENCONTRADA ---")
    print(f"Citação: {texto_citacao}")
    print(f"Autor: {autor_citacao}")
    print("--------------------------\n")

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    # --- Finalização ---
    print("Script finalizado. Fechando o navegador em 5 segundos.")
    # Mantém o navegador aberto por 5 segundos para visualização
    # time.sleep(5) # Se quiser usar, precisa importar a biblioteca 'time'
    driver.quit()