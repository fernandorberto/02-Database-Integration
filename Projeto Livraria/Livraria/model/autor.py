import re


class Autor:
    #def __init__(self) -> None:
    def __init__(self, nome: str, email: str, telefone: str, bio: str):
        self.__id: int = 0
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.bio = bio

        #self.__id = None
        #self.__nome = None
        #self.__email = None
        #self.__telefone = None
        #self.__bio = None

    def __eq__(self, value):
        return self.id == value

    def __str__(self):
        return f'{self.id} | {self.nome} | {self.email} | {self.telefone}'

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nome(self):  # getter
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.strip().title()

    @property
    def email(self):  # getter
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email.strip().lower()

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        if re.match('^\+55\d\d9\d\d\d\d-\d\d\d\d$', telefone):
            self.__telefone = telefone
        else:
            raise Exception('Número de telefone inválido.')

    @property
    def bio(self):
        return self.__bio

    @bio.setter
    def bio(self, bio):
        self.__bio = bio
