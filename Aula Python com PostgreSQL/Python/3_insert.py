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

def insert_data_into_table(connection, table_name, fields, values):
    try:
        cursor = connection.cursor()
        # Formatar os campos e criar placeholders para os valores
        query = (
        f"INSERT INTO {table_name} ({', '.join(fields)}) "
        #f"VALUES ({', '.join(['%s'] * len(values))});"
        f"VALUES (%s, %s, %s, %s, %s);"
        )
        print(f"Query gerada: {query, values}")
        # Executar a query, passando os valores
        cursor.execute(query, values)
        connection.commit()
        
        cursor.close()
    except Exception as error:
        print(f"Erro ao inserir dados: {error}")

connection = get_connection()

# Tabelas que você quer inserir os dados
tabela = 'vendas.produtos'
campos = ['id_produto, nome, descricao, preco, id_categoria']
valores = (15,'Blusa Infantil Solar','',129.9,1)

insert_data_into_table(connection, tabela, campos, valores)

close_connection(connection)