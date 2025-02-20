import os

# Parâmetros do banco de dados
DB_PARAMS = {
    "dbname": "brt_db",
    "user": "admin",
    "password": "admin",
    "host": "localhost",
    "port": "5432"
}

# URLs e caminhos dos arquivos
API_URL = "https://dados.mobilidade.rio/gps/brt"
DATA_DIR = "data"
JSON_FILE_PATH = os.path.join(DATA_DIR, "veiculos.json")
CSV_FILE_PATH = os.path.join(DATA_DIR, "veiculos.csv")
TABLE_NAME = "brt_veiculos"

# Garantir que a pasta "data" exista
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
