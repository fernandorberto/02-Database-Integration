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

def delete_data_from_table(connection, table_name, condition_column, condition_value):
    try:
        cursor = connection.cursor()
        query = f"DELETE FROM {table_name} WHERE {condition_column} = %s;"
        cursor.execute(query, (condition_value,))
        rows_deleted = cursor.rowcount  # Verifica quantas linhas foram afetadas
        connection.commit()       
         
        if rows_deleted > 0:
            print(f"Dados com {condition_column} = {condition_value} foram excluídos com sucesso.")
        else:
            print(f"Nenhum dado encontrado com {condition_column} = {condition_value}.")
                
        cursor.close()
    except Exception as error:
        print(f"Erro ao excluir dados: {error}")

connection = get_connection()

# Tabelas que você quer buscar os dados
tabela = 'vendas.produtos'
coluna_condicao = 'id_produto'
valor_condicao = 15  # Esse valor pode ser alterado dinamicamente
    
# Deletar dados da tabela
delete_data_from_table(connection, tabela, coluna_condicao, valor_condicao)

close_connection(connection)