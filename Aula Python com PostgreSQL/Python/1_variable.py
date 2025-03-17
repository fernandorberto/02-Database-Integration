import psycopg2
import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

# Acessar o Host definidos no .env
host = os.getenv("PGHOST")

# Verificar se o host foi carregado corretamente
if host:
    print(f"Host carregado: {host}")
else:
    print("Erro: Host não foi encontrado no arquivo .env")