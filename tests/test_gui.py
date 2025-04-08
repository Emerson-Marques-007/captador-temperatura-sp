import pytest
from tkinter import Tk
from src.gui import WeatherApp

@pytest.fixture
def app():
    root = Tk()
    app = WeatherApp(root)
    yield app
    root.destroy()

def test_widgets_creation(app):
    assert app.fetch_btn is not None
    assert app.status_var is not None
    assert app.date_label is not None
    assert app.temp_label is not None
    assert app.humidity_label is not None
    assert app.status_label is not None

def test_initial_status(app):
    """Verifica o estado inicial dos widgets."""
    assert app.status_var.get() == "Pronto para buscar dados"
    assert app.date_label.cget("text") == "--/--/----"
    assert app.temp_label.cget("text") == "-- °C"
    assert app.humidity_label.cget("text") == "-- %"
    assert app.status_label.cget("text") == "--"

