import pandas as pd
import json
from config_brt import JSON_FILE_PATH, CSV_FILE_PATH

def transform_data():
    """Carrega dados JSON, transforma e salva como CSV."""
    with open(JSON_FILE_PATH, "r") as json_file:
        data = json.load(json_file)

    # Acessar lista de veículos
    veiculos = data.get("veiculos", [])
    df = pd.DataFrame(veiculos)

    # Converter dataHora para timestamp
    if "dataHora" in df.columns:
        df["dataHora"] = pd.to_datetime(df["dataHora"], unit="ms")

    # Substituir NaN e pd.NA por None
    df = df.where(pd.notna(df), None)

    # Ajustar ignicao para string
    if "ignicao" in df.columns:
        df["ignicao"] = df["ignicao"].apply(lambda x: str(int(x)) if pd.notna(x) else None)

    # Salvar CSV
    df.to_csv(CSV_FILE_PATH, index=False)
    print(f"Arquivo CSV transformado salvo em {CSV_FILE_PATH}")

if __name__ == "__main__":
    transform_data()
