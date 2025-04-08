import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WeatherScraper:
    def __init__(self):
        self.driver = None
        self.initialize_driver()
        
    def initialize_driver(self):
        try:
            edge_options = EdgeOptions()
            edge_options.add_argument("--headless")  # Executar em modo headless (sem interface gráfica)
            edge_options.add_argument("--disable-gpu")
            edge_options.add_argument("--no-sandbox")
            edge_options.add_argument("--disable-dev-shm-usage")  # Reduz problemas de memória compartilhada
            edge_options.add_argument("--proxy-server='direct://'")
            edge_options.add_argument("--proxy-bypass-list=*")

            self.driver = webdriver.Edge(
                service=EdgeService(EdgeChromiumDriverManager().install()),
                options=edge_options
            )
            self.driver.set_page_load_timeout(30)
        except Exception as e:
            logging.error(f"Erro ao iniciar o WebDriver: {str(e)}")
            raise

    def get_weather_data(self):
        try:
            self.driver.get('https://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp')
            logging.info("Página carregada com sucesso.")
            
            # Espera explícita para o elemento de temperatura
            temp_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="max-temp-1"]'))  # Substitua pelo XPath correto
            )
            humidity_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="mainContent"]/div[7]/div[3]/div[1]/div[2]/div[2]/div[3]/div[1]/ul/li[4]/div/p/span[2]'))  # Substitua pelo XPath correto
            )
            
            temperature = temp_element.text.replace('°', '').strip()
            humidity = humidity_element.text.replace('%', '').strip()
            
            logging.info(f"Temperatura: {temperature} °C, Umidade: {humidity} %")
            return {
                'temperature': float(temperature),
                'humidity': float(humidity)
            }
        except Exception as e:
            logging.error(f"Erro ao localizar elementos na página: {str(e)}")
            return None
        finally:
            if self.driver:
                self.driver.quit()