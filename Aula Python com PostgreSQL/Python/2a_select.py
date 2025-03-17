import psycopg2
import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

# Busca dados conexão
def get_connection():
    connection = psycopg2.connect(
        host=os.getenv('PGHOST'),
        database=os.getenv('PGDATABASE'),
        user=os.getenv('PGUSER'),
        password=os.getenv('PGPASSWORD'),
        sslmode="require"
    )
    print("Conexão estabelecida!")
    return connection

def close_connection(connection):
    if connection:
        connection.close()
        print("Conexão fechada!")

def fetch_data_from_table(connection, table_name):
    try:
        cursor = connection.cursor()
        query = f"SELECT * FROM {table_name} ORDER BY id_produto;"
        cursor.execute(query)
        records = cursor.fetchall()
        
        # Antes do loop, mapeie os nomes das colunas para seus índices
        column_names = [desc[0] for desc in cursor.description]
        column_index = column_names.index('nome')  # Substitua pelo nome da coluna desejada

        # Exibir os resultados
        for row in records:
            print(row[column_index])
        # Exibir os resultados
        #for row in records:
        #    print(row)
        
        cursor.close()
    except Exception as error:
        print(f"Erro ao buscar dados: {error}")

connection = get_connection()

# Tabelas que você quer buscar os dados
tabelas = ['leandro_fonseca.produtos']

for tabela in tabelas:
    print(f"\nDados da tabela {tabela}:")
    fetch_data_from_table(connection, tabela)

close_connection(connection)

