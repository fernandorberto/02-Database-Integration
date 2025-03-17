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

def fetch_clientes(connection, nome_cliente):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM vendas.clientes WHERE Nome ILIKE %s;"
        cursor.execute(query, (f'%{nome_cliente}%',))
        results = cursor.fetchall()
        cursor.close()
        return results
    except Exception as error:
        print(f"Erro ao buscar clientes: {error}")
        return []

def update_descricao(connection, id_cliente, nova_descricao):
    try:
        cursor = connection.cursor()
        query = "UPDATE vendas.Clientes SET nome = %s WHERE id_cliente = %s;"
        cursor.execute(query, (nova_descricao, id_cliente))
        connection.commit()        
        
        cursor.close()
        print("Descrição atualizada com sucesso!")
    except Exception as error:
        print(f"Erro ao atualizar descrição: {error}")

connection = get_connection()

# Solicitar nome do cliente ao usuário
nome_cliente_input = input("Digite o nome do cliente: ")

# Buscar clientes
clientes = fetch_clientes(connection, nome_cliente_input)

if clientes:
    print("Clientes encontrados:")
    for cliente in clientes:
        print(cliente)  # Exibe informações do cliente (ajuste conforme necessário)
    
    # Solicitar ao usuário se deseja alterar a descrição
    alterar = input("Deseja alterar a descrição de algum cliente? (s/n): ")
    if alterar.lower() == 's':
        id_cliente = int(input("Digite o ID do cliente cuja descrição você deseja alterar: "))
        nova_descricao = input("Digite a novo descrição: ")
        
        # Atualizar descrição
        update_descricao(connection, id_cliente, nova_descricao)

else:
    print("Nenhum cliente encontrado com o nome fornecido.")

close_connection(connection)
