import pytest
from unittest.mock import patch, MagicMock

def test_initialization(scraper):
    assert scraper.driver is not None

@patch('selenium.webdriver.Chrome')
def test_get_weather_data_success(mock_chrome, scraper):
    # Configura o mock
    mock_driver = MagicMock()
    mock_chrome.return_value = mock_driver
    
    # Simula elementos da página
    mock_temp = MagicMock()
    mock_temp.text = "25°"
    mock_humidity = MagicMock()
    mock_humidity.text = "60%"
    
    mock_driver.find_element.side_effect = [mock_temp, mock_humidity]
    
    # Executa o teste
    result = scraper.get_weather_data()
    
    # Verificações
    assert result == {'temperature': 25.0, 'humidity': 60.0}
    mock_driver.get.assert_called_once()

def test_get_weather_data_failure(scraper):
    with patch.object(scraper.driver, 'get', side_effect=Exception("Erro")):
        result = scraper.get_weather_data()
        assert result is None
        # Verificar se o erro foi tratado corretamente
        scraper.driver.get.assert_called_once()