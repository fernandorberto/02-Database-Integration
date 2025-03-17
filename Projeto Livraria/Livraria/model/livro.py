import itertools

from model.autor import Autor
from model.categoria import Categoria
from model.editora import Editora


class Livro:
    def __init__(self,
                 titulo: str,
                 resumo: str,
                 ano: int,
                 paginas: int,
                 isbn: str,
                 categoria: Categoria,
                 editora: Editora,
                 autor: Autor) -> None:
        self.__id = 0
        self.titulo = titulo
        self.resumo = resumo
        self.ano = ano
        self.paginas = paginas
        self.isbn = isbn
        self.categoria = categoria
        self.editora = editora
        self.autor = autor
        
#    def __init__(self) -> None:
#        self.__id: int = None
#        self.__titulo: str = None
#        self.__resumo: str = None
#        self.__ano: int = None
#        self.__paginas: int = None
#        self.__isbn: str = None
#        self.__autor: Autor = None
#        self.__categoria: Categoria = None
#        self.__editora: Editora = None


    def __str__(self) -> str:
        return f'{self.id} | {self.titulo} | {self.resumo} | \
            {self.ano} | {self.paginas} | {self.isbn} | \
            {self.autor.nome} | {self.categoria.nome} | {self.editora.nome}'

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    @property
    def resumo(self) -> str:
        return self.__resumo

    @resumo.setter
    def resumo(self, resumo: str):
        self.__resumo = resumo

    @property
    def ano(self) -> int:
        return self.__ano

    @ano.setter
    def ano(self, ano: int):
        self.__ano = ano

    @property
    def paginas(self) -> int:
        return self.__paginas

    @paginas.setter
    def paginas(self, paginas: int):
        self.__paginas = paginas

    @property
    def isbn(self) -> str:
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn: str):
        self.__isbn = isbn

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor):
        self.__autor = autor

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria

    @property
    def editora(self):
        return self.__editora

    @editora.setter
    def editora(self, editora):
        self.__editora = editora
