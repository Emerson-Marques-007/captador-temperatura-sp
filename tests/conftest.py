import pytest
from src.weather_scraper import WeatherScraper
from src.data_handler import DataHandler
import os

@pytest.fixture
def temp_file(tmp_path):
    """Cria um arquivo temporário para testes"""
    file = tmp_path / "test_data.xlsx"
    yield file
    if os.path.exists(file):
        os.remove(file)

@pytest.fixture
def scraper():
    """Instância do WeatherScraper para testes"""
    return WeatherScraper()

@pytest.fixture
def data_handler(temp_file):
    """Instância do DataHandler com arquivo temporário"""
    return DataHandler(file_path=temp_file)