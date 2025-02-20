
# Instruções para Rodar o Processo

## Requisitos

1. **Docker**: Você precisa ter o Docker instalado e em funcionamento na sua máquina para rodar o banco de dados PostgreSQL localmente.
   
2. **Banco de Dados PostgreSQL**: O processo depende de um banco PostgreSQL que deve estar rodando em um contêiner Docker. Se você ainda não tiver o banco configurado, siga o passo a passo abaixo para configurar um contêiner Docker com PostgreSQL.

3. **Tabela Requerida**: Antes de rodar o processo, você precisa garantir que a tabela `brt_veiculos` exista no seu banco de dados. Para isso, execute o seguinte comando SQL:

   ```sql
   CREATE TABLE IF NOT EXISTS brt_veiculos (
       codigo VARCHAR(20),
       placa VARCHAR(20),
       linha VARCHAR(20),
       latitude double precision,
       longitude double precision,
       dataHora timestamp,
       velocidade double precision,
       sentido VARCHAR(10),
       trajeto varchar(100),
       hodometro double precision,
       direcao varchar(100),
       ignicao varchar(100)
   );
   ```

## Como Rodar o Processo

Para rodar o processo, basta executar o seguinte comando:

```bash
python main.py
```

Isso irá executar o processo com os dados do banco de dados configurado localmente.

## Como Configurar o Banco de Dados Docker (Caso não tenha configurado)

Se você ainda não configurou o banco de dados PostgreSQL no Docker, siga as instruções abaixo para fazer isso:

1. Crie o contêiner Docker com PostgreSQL executando o seguinte comando no terminal:

   ```bash
   docker run --name postgres-container -e POSTGRES_PASSWORD=admin -e POSTGRES_USER=admin -e POSTGRES_DB=brt_db -p 5432:5432 -d postgres
   ```

2. Certifique-se de que o contêiner PostgreSQL está rodando corretamente e configurado para aceitar conexões externas.

3. Crie a tabela `brt_veiculos` executando o comando SQL acima no seu banco de dados PostgreSQL.

4. Depois de configurar o banco de dados e a tabela, você pode rodar o processo com o comando `python main.py`.

---

Caso tenha dúvidas, entre em contato para mais informações.
