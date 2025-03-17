import os
from dotenv import load_dotenv
from openai import OpenAI

def gera_bio(autor):
    prompt = (f"Crie uma mini biografia do autor {autor}, "
              "destacando seus principais feitos, contribuições e informações relevantes sobre sua vida.")
    return prompt

# Carregar variáveis do arquivo .env
load_dotenv()

# Acessar a chave da API do OpenAI definida no .env
openai_api_key = os.getenv("OPENAI_API_KEY")

# Verificar se a chave foi carregada corretamente
#if openai_api_key:
#    print(f"Chave da API carregada: {openai_api_key}")
#else:
#    print("Erro: Chave da API não foi encontrada no arquivo .env")

client = OpenAI()
autor = input('Nome do autor: ')
prompt = gera_bio(autor)

if prompt:
    completion = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=[
            {"role": "system", 
             "content": "Você é um assistente literário especializado em criar biografias de autores."},
            {"role": "user", 
             "content": prompt}
        ]
    )
    
    print(completion.choices[0].message)
else:
    print("Erro: O prompt gerado está vazio.")
