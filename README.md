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

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv env
   source env/bin/activate # No Windows: env\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Como Iniciar o Programa

1. Execute o programa principal:
   ```bash
   python src/main.py
   ```

2. A interface gráfica será exibida, permitindo que você colete e visualize os dados de temperatura e umidade.

## Requisitos

- Python 3.10 ou superior.
- Microsoft Edge (última versão).
- EdgeDriver (gerenciado automaticamente pelo `webdriver-manager`).

## Solução de Problemas

Se encontrar erros relacionados ao Selenium, atualize o EdgeDriver:
```bash
pip install --upgrade webdriver-manager
```

## Capturas de Tela

### Tela Inicial
![Tela Inicial](docs/tela_inicial.png)

### Dados Atualizados
![Dados Atualizados](docs/dados_atualizados.png)