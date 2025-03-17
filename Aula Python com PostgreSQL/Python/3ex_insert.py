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
            f"VALUES ({', '.join(['%s'] * len(values))});"
        )
        print(f"Query gerada: {query}")
        # Executar a query, passando os valores
        cursor.execute(query, values)
        connection.commit()
        print("Dados inseridos com sucesso!")
        cursor.close()
    except Exception as error:
        print(f"Erro ao inserir dados: {error}")

# Função para coletar dados do usuário
def get_user_input():
    id_cliente = int(input("Digite o ID do cliente: "))
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = int(input("Digite o telefone do cliente (somente números): "))
    endereco = input("Digite o endereço do cliente: ")
    cpf = int(input("Digite o CPF do cliente (somente números): "))
    ddd = input("Digite o DDD do telefone: ")
    return (id_cliente, nome, email, telefone, endereco, cpf, ddd)

# Main
connection = get_connection()

# Tabela e campos
tabela = 'vendas.clientes'
campos = ['id_cliente', 'nome', 'email', 'telefone', 'endereco', 'cpf', 'ddd']

# Coleta de dados via input do usuário
valores = get_user_input()

# Inserção dos dados na tabela
insert_data_into_table(connection, tabela, campos, valores)

# Fechar a conexão
close_connection(connection)
