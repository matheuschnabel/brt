import requests
import json
from prefect import Flow, task
from config_brt import API_URL, JSON_FILE_PATH

@task
def fetch_data_from_api():
    """Faz a requisição à API e retorna os dados JSON."""
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao acessar a API: {response.status_code}")

@task
def save_json_data(data):
    """Salva os dados JSON no arquivo."""
    with open(JSON_FILE_PATH, "w") as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Arquivo JSON salvo em {JSON_FILE_PATH}")

# Criando fluxo do Prefect
with Flow("API_to_JSON_Flow") as flow:
    data = fetch_data_from_api()
    save_json_data(data)

if __name__ == "__main__":
    flow.run()
