from selenium import webdriver
import time

# --- Configuração ---
driver = webdriver.Chrome()

# Maximiza a janela para uma screenshot melhor
driver.maximize_window()

# --- Ação ---
try:
    print("Acessando o site do gov.br...")
    driver.get("https://www.instagram.com/andrey.barfknecht/")
    time.sleep(3) # Espera a página carregar completamente com as imagens

    # Define o nome do arquivo da screenshot
    nome_do_arquivo = "prin_insta.png"

    # Tira a screenshot e salva
    driver.save_screenshot(nome_do_arquivo)
    print(f"Screenshot salva com sucesso como '{nome_do_arquivo}'!")
    print("Verifique o arquivo na mesma pasta onde o script foi executado.")

except Exception as e:
    print(f"Ocorreu um erro ao tirar a screenshot: {e}")

finally:
    # --- Finalização ---
    time.sleep(2)
    driver.quit()