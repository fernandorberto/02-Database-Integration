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

# Função para buscar dados da tabela Clientes com filtro pelo nome
def fetch_data_by_name(connection, name):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM vendas.clientes WHERE nome ILIKE %s;"  # Usando ILIKE para case-insensitive
        cursor.execute(query, (f'{name}%',))
        records = cursor.fetchall()
        
        # Exibir os resultados
        if records:
            for row in records:
                print(row)
        else:
            print(f"Nenhum cliente encontrado com o nome contendo '{name}'")
        
        cursor.close()
    except Exception as error:
        print(f"Erro ao buscar dados: {error}")

# Estabelece conexão
connection = get_connection()

# Recebe o nome do cliente via input do usuário
nome_cliente = input("Digite o nome do cliente para buscar: ")

# Busca os dados da tabela Clientes pelo nome
fetch_data_by_name(connection, nome_cliente)

# Fecha conexão
close_connection(connection)