import os

# Definir caminho base dos scripts
SCRIPTS_DIR = "scripts"

print("🚀 Iniciando o pipeline ETL...")

# Executar extração
print("📥 Extraindo dados da API...")
os.system(f"python {SCRIPTS_DIR}/extract_flow.py")

# Executar transformação
print("🔄 Transformando dados...")
os.system(f"python {SCRIPTS_DIR}/transform_brt.py")

# Executar carga no banco de dados
print("📤 Carregando dados no PostgreSQL...")
os.system(f"python {SCRIPTS_DIR}/load_to_bd.py")

print("✅ Pipeline concluído com sucesso!")
