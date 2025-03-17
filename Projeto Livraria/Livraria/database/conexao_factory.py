import psycopg2

from os import getenv
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

class ConexaoFactory:
    def get_conexao(self):
        return psycopg2.connect(
            host=getenv('PGHOST'),
            database=getenv('PGDATABASE'),
            user=getenv('PGUSER'),
            password=getenv('PGPASSWORD')
        )