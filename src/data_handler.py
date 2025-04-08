import pandas as pd
import os
from datetime import datetime

class DataHandler:
    def __init__(self, file_path="data/temperature_data.xlsx"):
        self.file_path = file_path
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        if not os.path.exists(self.file_path):
            self.create_file()

    def create_file(self):
        df = pd.DataFrame(columns=["Data", "Hora", "Temperatura (°C)", "Umidade (%)", "Status Umidade"])
        df.to_excel(self.file_path, index=False, engine="openpyxl")

    def save_weather_data(self, temperature, humidity):
        now = datetime.now()
        status = self.get_humidity_status(humidity)
        new_data = {
            "Data": [now.strftime("%d/%m/%Y")],
            "Hora": [now.strftime("%H:%M:%S")],
            "Temperatura (°C)": [temperature],
            "Umidade (%)": [humidity],
            "Status Umidade": [status],
        }
        df = pd.DataFrame(new_data)
        if os.path.exists(self.file_path):
            existing_df = pd.read_excel(self.file_path, engine="openpyxl")
            df = pd.concat([existing_df, df], ignore_index=True)
        df.to_excel(self.file_path, index=False, engine="openpyxl")

    def get_humidity_status(self, humidity):
        if humidity < 30:
            return "Baixa"
        elif 30 <= humidity <= 70:
            return "Normal"
        else:
            return "Alta"