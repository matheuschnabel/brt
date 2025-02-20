import pandas as pd
import psycopg2
from psycopg2 import sql
from config_brt import DB_PARAMS, CSV_FILE_PATH, TABLE_NAME

def load_csv_to_postgres():
    """Carrega CSV e insere os dados no banco PostgreSQL."""
    df = pd.read_csv(CSV_FILE_PATH)

    # Conectar ao banco
    conn = psycopg2.connect(**DB_PARAMS)
    cursor = conn.cursor()

    # Query de inserção
    insert_query = sql.SQL("""
        INSERT INTO {} (codigo, placa, linha, latitude, longitude, dataHora, velocidade, sentido, trajeto, hodometro, direcao, ignicao)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """).format(sql.Identifier(TABLE_NAME))

    # Inserir os dados
    for _, row in df.iterrows():
        cursor.execute(insert_query, (
            row["codigo"], row["placa"], row["linha"], row["latitude"], row["longitude"], row["dataHora"],
            row["velocidade"], row["sentido"], row["trajeto"], row["hodometro"], row["direcao"], row["ignicao"]
        ))

    # Commit e fechamento
    conn.commit()
    cursor.close()
    conn.close()
    print("Dados inseridos com sucesso!")

if __name__ == "__main__":
    load_csv_to_postgres()
