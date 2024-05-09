# chrome_interaction.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class RobosEA:
    def __init__(self):
        self.driver = None
    
    def start_chrome(self):
        # Iniciar o Chrome com Selenium
        chrome_driver_path = "/usr/bin/chromedriver"  # Caminho para o ChromeDriver
        chrome_service = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=chrome_service)
    
    def open_url(self, url):
        # Abrir uma URL no Chrome
        if not self.driver:
            raise Exception("Chrome não iniciado. Chame 'start_chrome()' primeiro.")
        self.driver.get(url)
    
    def close_chrome(self):
        # Fechar o Chrome
        if self.driver:
            self.driver.quit()
            self.driver = None
