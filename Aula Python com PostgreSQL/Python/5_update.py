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

def update_product_name(connection, table_name, condition_column, condition_value, new_product_name):
    try:
        cursor = connection.cursor()
        query = f"UPDATE {table_name} SET nome = %s WHERE {condition_column} = %s;"
        cursor.execute(query, (new_product_name, condition_value))
        connection.commit()        
        
        cursor.close()
        print("Nome do produto atualizado com sucesso!")
    except Exception as error:
        print(f"Erro ao atualizar nome do produto: {error}")

connection = get_connection()

# Parâmetros
tabela = 'vendas.produtos'
coluna_condicao = 'id_produto'
valor_condicao = 3  # Esse valor pode ser alterado dinamicamente
novo_nome_produto = 'Camiseta Infantil Solar'  # Nome que você quer atualizar

# Atualizar nome do produto
update_product_name(connection, tabela, coluna_condicao, valor_condicao, novo_nome_produto)

close_connection(connection)
