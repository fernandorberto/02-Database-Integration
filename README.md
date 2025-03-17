# 📚 Database Integration com Python e PostgreSQL

Este repositório contém estudos e práticas sobre **integração com bancos de dados** usando Python, focando no **PostgreSQL** com a biblioteca `psycopg2`. Também abordamos conceitos de **DDL e DML em SQL**, além de um **projeto final** de uma **livraria integrada a um banco provisionado no Render**.

## 🚀 Tecnologias Utilizadas

- **Python** 🐍  
- **PostgreSQL** 🗄️  
- **Psycopg2** 🔗  
- **SQL (DDL e DML)** 💾  
- **Render (Provisionamento do Banco de Dados)** ☁️  

## 🏗️ Estrutura do Repositório

```
📂 02-Database-Integration
 ├── 📂 Aula Python com PostgreSQL
 │   ├── 1_variable.py
 │   ├── 2_select.py
 │   ├── 3_insert.py
 │   ├── 4_delete.py
 │   ├── 5_update.py
 │   ├── join_python.py
 │   ├── requirements.txt
 │   ├── .env
 │   ├── __pycache__/
 │   └── ...
 ├── 📂 Projeto Livraria
 │   ├── 📂 dao/
 │   ├── 📂 database/
 │   ├── 📂 model/
 │   ├── 📂 service/
 │   ├── 📂 sql/
 │   ├── .env
 │   ├── main.py
 │   ├── README.md
 │   └── .gitignore
```

## 📌 Conceitos Abordados  

✔️ **DDL (Data Definition Language)**  
- `CREATE TABLE`  
- `ALTER TABLE`  
- `DROP TABLE`  

✔️ **DML (Data Manipulation Language)**  
- `INSERT`  
- `SELECT`  
- `UPDATE`  
- `DELETE`  

✔️ **Conexão com PostgreSQL** via `psycopg2`  
✔️ **Execução de Queries SQL no Python**  
✔️ **Provisionamento do Banco de Dados no Render**  

## 📂 Como Executar o Projeto  

```bash
# 1️⃣ Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git

# 2️⃣ Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

# 3️⃣ Instale as dependências
pip install -r requirements.txt

# 4️⃣ Configure o Banco de Dados
# - Provisionar um banco PostgreSQL no Render
# - Copiar as credenciais geradas para o arquivo .env

# 5️⃣ Execute o projeto
python main.py
```

## ☁️ Provisionamento do Banco no Render  

O banco de dados **PostgreSQL** foi provisionado no **Render**. Para conectar o projeto:  

1️⃣ Criar um banco no Render  
2️⃣ Copiar as credenciais fornecidas  
3️⃣ Inserir as informações no arquivo `.env` do projeto  

---

💡 **Projeto criado para estudos e aprimoramento em Python e bancos de dados.** 🚀  
