# Dentro do seu módulo ou script Python

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class MyLibrary:
    def __init__(self):
        # Configurar o Selenium para usar o ChromeDriver
        chrome_driver_path = "/usr/bin/chromedriver"
        chrome_service = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=chrome_service)
    
    def open_url(self, url):
        # Abrir uma URL no Chrome
        self.driver.get(url)
    
    def close(self):
        # Fechar o navegador
        self.driver.quit()
