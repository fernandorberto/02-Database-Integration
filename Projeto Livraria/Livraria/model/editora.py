import itertools


class Editora:
    id_iter = itertools.count(start=1)

    def __init__(self, nome: str, endereco: str, telefone: str):
        self.__id: int = next(Editora.id_iter)
        self.__nome: str = nome
        self.__endereco: str = endereco
        self.__telefone: str = telefone

    def __str__(self) -> str:
        return f'{self.id} | {self.nome} | {self.endereco} | {self.telefone}'

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def endereco(self) -> str:
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco: str):
        self.__endereco = endereco

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone
