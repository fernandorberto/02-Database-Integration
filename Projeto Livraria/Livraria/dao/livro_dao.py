#import itertools
from model.livro import Livro
from dao.autor_dao import AutorDAO
from dao.categoria_dao import CategoriaDAO
from dao.editora_dao import EditoraDAO
from database.conexao_factory import ConexaoFactory


class LivroDAO:
    #_indice_tabela_livros = itertools.count(start=1)
    #_tabela_livros: list[Livro] = []

    def __init__(self) -> None:
        self.__conexao_factory = ConexaoFactory()
        self.__categoria_dao = CategoriaDAO()
        self.__editora_dao = EditoraDAO()
        self.__autor_dao = AutorDAO()
    #    pass

    def get_all(self) -> list[Livro]:
        livros = list()
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, titulo, resumo, ano, paginas, isbn, id_categoria, id_editora, id_autor FROM lf_livraria.livros")
        resultados = cursor.fetchall()
        for resultado in resultados:
            categoria = self.__categoria_dao.buscar_por_id(resultado[6])
            editora = self.__editora_dao.buscar_por_id(resultado[7])
            autor = self.__autor_dao.buscar_por_id(resultado[8])

            livro = Livro(resultado[1], resultado[2], resultado[3], resultado[4], resultado[5], categoria, editora, autor)
            livro.id = resultado[0]

            livros.append(livro)

        cursor.close()
        conexao.close()

        return livros
    #    return self._tabela_livros

    def adicionar(self, livro: Livro) -> None:
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO lf_livraria.livros(titulo, resumo, ano, paginas, isbn, id_categoria, id_editora, id_autor) " \
            "VALUES (%(t)s, %(r)s, %(a)s, %(p)s, %(i)s, %(ci)s, %(ei)s, %(ai)s)",
            {'t': livro.titulo, 'r': livro.resumo, 'a': livro.ano, 'p': livro.paginas, 'i': livro.isbn,
             'ci': livro.categoria.id, 'ei': livro.editora.id, 'ai': livro.autor.id }
        )
        conexao.commit()
        cursor.close()
        conexao.close()

        #livro.id = next(self._indice_tabela_livros)
        #self._tabela_livros.append(livro)

    def remover(self, livro_id: int) -> bool:
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"DELETE FROM lf_livraria.livros WHERE id = {livro_id}")
        livros_removidos = cursor.rowcount
        conexao.commit()
        cursor.close()
        conexao.close()

        if livros_removidos:
            return True

        return False
    
        #for livro in self._tabela_livros:
        #    if livro.id == livro_id:
        #        index = self._tabela_livros.index(livro)
        #        self._tabela_livros.pop(index)
        #        return True

        #return False

    def buscar_por_id(self, livro_id) -> Livro:
        livro = None
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"SELECT id, titulo, resumo, ano, paginas, isbn, id_categoria, id_editora, id_autor FROM lf_livraria.livros where id = {livro_id}")
        resultado = cursor.fetchone()
        if resultado:
            categoria = self.__categoria_dao.buscar_por_id(resultado[6])
            editora = self.__editora_dao.buscar_por_id(resultado[7])
            autor = self.__autor_dao.buscar_por_id(resultado[8])

            livro = Livro(resultado[1], resultado[2], resultado[3], resultado[4], resultado[5], categoria, editora, autor)
            livro.id = resultado[0]

        cursor.close()
        conexao.close()
        return livro
        #for livro in self._tabela_livros:
        #    if livro.id == livro_id:
        #        return livro

        #return False
