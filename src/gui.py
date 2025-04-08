import os
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from datetime import datetime
from weather_scraper import WeatherScraper
from data_handler import DataHandler
import threading
import queue

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Captador de Temperatura - SP")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#f5f5f5")

        self.scraper = WeatherScraper()
        self.data_handler = DataHandler()
        self.queue = queue.Queue()

        self.setup_ui()

    def setup_ui(self):
        # Cabeçalho com ícone
        header_frame = ttk.Frame(self.root, padding=10)
        header_frame.pack(fill=tk.X)

        # Verifica se o arquivo de ícone existe
        icon_path = "icon.png"
        if os.path.exists(icon_path):
            icon = PhotoImage(file=icon_path)
        else:
            icon = None  # Ícone alternativo ou nenhum ícone

        if icon:
            ttk.Label(header_frame, image=icon).pack(side=tk.LEFT, padx=5)
            self.root.icon_image = icon  # Evita que o ícone seja coletado pelo garbage collector

        ttk.Label(
            header_frame,
            text="Captador de Temperatura",
            font=("Helvetica", 18, "bold"),
            background="#f5f5f5",
        ).pack(side=tk.LEFT, padx=10)

        # Botão de busca estilizado
        self.fetch_btn = ttk.Button(
            self.root,
            text="Buscar Dados",
            command=self.start_fetch_thread,
            style="Accent.TButton",
        )
        self.fetch_btn.pack(pady=20)

        # Status
        self.status_var = tk.StringVar(value="Pronto para buscar dados")
        ttk.Label(
            self.root,
            textvariable=self.status_var,
            font=("Helvetica", 12),
            background="#f5f5f5",
        ).pack(pady=10)

        # Resultados
        self.result_frame = ttk.LabelFrame(
            self.root, text="Últimos Dados", padding=10, style="Modern.TLabelframe"
        )
        self.result_frame.pack(fill=tk.X, padx=20, pady=20)

        self.date_label = self.create_result_row("Data:")
        self.time_label = self.create_result_row("Hora:")
        self.temp_label = self.create_result_row("Temperatura:")
        self.humidity_label = self.create_result_row("Umidade:")
        self.status_label = self.create_result_row("Status:")

        # Estilo personalizado
        style = ttk.Style()
        style.configure("Accent.TButton", font=("Helvetica", 12), background="#0078D7")
        style.configure("Modern.TLabelframe", font=("Helvetica", 12), background="#f5f5f5")

    def create_result_row(self, label_text):
        row_frame = ttk.Frame(self.result_frame)
        row_frame.pack(fill=tk.X, pady=5)
        ttk.Label(row_frame, text=label_text, width=15, anchor="w").pack(side=tk.LEFT)
        value_label = ttk.Label(row_frame, text="--", font=("Helvetica", 12))
        value_label.pack(side=tk.LEFT)
        return value_label

    def start_fetch_thread(self):
        self.fetch_btn.config(state=tk.DISABLED)
        self.status_var.set("Buscando dados...")
        thread = threading.Thread(target=self.fetch_weather_data)
        thread.start()
        self.monitor_thread(thread)

    def monitor_thread(self, thread):
        if thread.is_alive():
            self.root.after(100, lambda: self.monitor_thread(thread))
        else:
            self.fetch_btn.config(state=tk.NORMAL)
            try:
                result = self.queue.get_nowait()
                if isinstance(result, Exception):
                    self.status_var.set(f"Erro: {str(result)}")
                else:
                    self.update_ui(result)
            except queue.Empty:
                self.status_var.set("Erro desconhecido.")

    def fetch_weather_data(self):
        try:
            weather_data = self.scraper.get_weather_data()
            if not weather_data:
                raise ValueError("Nenhum dado retornado pelo scraper.")
            self.data_handler.save_weather_data(weather_data["temperature"], weather_data["humidity"])
            self.queue.put(weather_data)
        except Exception as e:
            self.queue.put(e)

    def update_ui(self, weather_data):
        now = datetime.now()
        self.date_label.config(text=now.strftime("%d/%m/%Y"))
        self.time_label.config(text=now.strftime("%H:%M:%S"))
        self.temp_label.config(text=f"{weather_data['temperature']} °C")
        self.humidity_label.config(text=f"{weather_data['humidity']} %")
        self.status_label.config(text=self.data_handler.get_humidity_status(weather_data["humidity"]))
        self.status_var.set("Dados atualizados com sucesso!")