# Captador de Temperatura - São Paulo

Aplicação para captura automática de dados de temperatura e umidade de São Paulo.

![Interface](docs/interface.png)

## Funcionalidades

- Coleta temperatura e umidade atual.
- Armazena dados históricos em Excel.
- Interface gráfica moderna e amigável.
- Classificação automática do status de umidade.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/captador-temperatura-sp.git
   cd captador-temperatura-sp
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute a aplicação:
   ```bash
   python src/gui.py
   ```

## Requisitos

- Python 3.10 ou superior.
- Google Chrome (última versão).
- ChromeDriver (gerenciado automaticamente pelo `webdriver-manager`).

## Solução de Problemas

Se encontrar erros relacionados ao Selenium, atualize o ChromeDriver:
```bash
pip install --upgrade webdriver-manager
```

## Capturas de Tela

### Tela Inicial
![Tela Inicial](docs/tela_inicial.png)

### Dados Atualizados
![Dados Atualizados](docs/dados_atualizados.png)