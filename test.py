from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

try:
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    driver.get("https://www.google.com")
    print(driver.title)
    driver.quit()
except Exception as e:
    print(f"Erro ao iniciar o Edge WebDriver: {str(e)}")