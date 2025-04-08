import pandas as pd
from datetime import datetime

def test_file_creation(data_handler, temp_file):
    """Verifica se o arquivo é criado com colunas corretas"""
    df = pd.read_excel(temp_file)
    expected_columns = ['Data', 'Hora', 'Temperatura (°C)', 'Umidade (%)', 'Status Umidade']
    assert list(df.columns) == expected_columns

def test_save_weather_data(data_handler):
    """Testa a gravação de dados no arquivo"""
    test_data = {
        'temperature': 22.5,
        'humidity': 45.0
    }
    
    success = data_handler.save_weather_data(**test_data)
    assert success
    
    df = pd.read_excel(data_handler.file_path)
    assert len(df) == 1
    assert df.iloc[0]['Temperatura (°C)'] == 22.5

def test_humidity_status(data_handler):
    """Testa a classificação da umidade"""
    assert data_handler.get_humidity_status(25) == "Baixa"
    assert data_handler.get_humidity_status(50) == "Normal"
    assert data_handler.get_humidity_status(80) == "Alta"