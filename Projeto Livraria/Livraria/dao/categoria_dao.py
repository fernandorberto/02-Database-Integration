#import itertools
from model.categoria import Categoria
from database.conexao_factory import ConexaoFactory

class CategoriaDAO:
    #_id_categoria = itertools.count(start=1)
    #_tabela_categorias: list[Categoria] = list()  # Tabela Categoria no banco de dados

    def __init__(self) -> None:
        self.__conexao_factory = ConexaoFactory()
        #pass

    def get_all(self) -> list[Categoria]:  # SELECT * FROM categoria
        categorias = list()

        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT id, nome FROM lf_livraria.categorias')
        resultados = cursor.fetchall()
        for resultado in resultados:
            cat = Categoria(resultado[1])
            cat.id = resultado[0]
            categorias.append(cat)

        cursor.close()
        conexao.close()

        return categorias
#        return self._tabela_categorias

    def adicionar(self, categoria: Categoria) -> None:  # INSERT INTO categoria
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO lf_livraria.categorias (nome) VALUES (%(n)s)", {'n': categoria.nome})
        conexao.commit()
        cursor.close()
        conexao.close()

    #    categoria.id = next(self._id_categoria)
    #    self._tabela_categorias.append(categoria)

    def remover(self, categoria_id: int) -> bool:
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute(f'DELETE FROM lf_livraria.categorias WHERE id = {categoria_id}')
        categorias_removidas = cursor.rowcount
        conexao.commit()
        cursor.close()
        conexao.close()

        if categorias_removidas == 0:
            return False

        return True
    
    #    for index, categoria in enumerate(self._tabela_categorias):
    #        if categoria.id == categoria_id:
    #            self._tabela_categorias.pop(index)
    #            return True

    #    return False

    def buscar_por_id(self, categoria_id) -> bool | Categoria:
        categoria = None
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute(f'SELECT id, nome FROM lf_livraria.categorias where id = {categoria_id}')
        resultado = cursor.fetchone()
        if resultado:
            categoria = Categoria(resultado[1])
            categoria.id = resultado[0]

        cursor.close()
        conexao.close()

        return categoria
        #for categoria in self._tabela_categorias:
        #    if categoria.id == categoria_id:
        #        return categoria

        #return False
