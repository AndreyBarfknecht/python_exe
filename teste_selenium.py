from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.instagram.com")
time.sleep(2)
caixa_pesquisa = driver.find_element(By.NAME, "q")
caixa_pesquisa.send_keys("Selenium Python")
caixa_pesquisa.send_keys(Keys.RETURN)
time.sleep(5)
driver.quit()