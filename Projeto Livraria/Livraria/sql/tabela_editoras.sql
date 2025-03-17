-- Tabela editoras
CREATE TABLE editoras (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    endereco TEXT,
    telefone VARCHAR(20)
);

