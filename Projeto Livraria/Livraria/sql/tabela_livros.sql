-- Tabela livros
CREATE TABLE livros (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    resumo TEXT,
    ano INT,
    paginas INT,
    isbn VARCHAR(20),
    id_categoria BIGINT,
    id_editora BIGINT,
    id_autor BIGINT,
    CONSTRAINT fk_categoria FOREIGN KEY (id_categoria) REFERENCES categorias(id),
    CONSTRAINT fk_editora FOREIGN KEY (id_editora) REFERENCES editoras(id),
    CONSTRAINT fk_autor FOREIGN KEY (id_autor) REFERENCES autores(id)
);