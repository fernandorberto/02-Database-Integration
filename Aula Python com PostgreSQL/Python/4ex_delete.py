import psycopg2 
import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

# Função para obter conexão com o banco de dados
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

# Função para fechar a conexão com o banco de dados
def close_connection(connection):
    if connection:
        connection.close()
        print("Conexão fechada!")

# Função para excluir dados da tabela com base em uma condição
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

# Estabelecer a conexão com o banco de dados
connection = get_connection()

# Tabela e coluna a serem usadas
tabela = 'vendas.clientes'
coluna_condicao = 'id_cliente'

# Solicitar ao usuário o ID do cliente a ser excluído
valor_condicao = input("Digite o ID do cliente que deseja excluir: ")

# Verificar se o valor digitado é um número
if valor_condicao.isdigit():
    valor_condicao = int(valor_condicao)  # Converter para inteiro
    delete_data_from_table(connection, tabela, coluna_condicao, valor_condicao)
else:
    print("Erro: O ID do cliente deve ser um número válido.")

# Fechar a conexão
close_connection(connection)
