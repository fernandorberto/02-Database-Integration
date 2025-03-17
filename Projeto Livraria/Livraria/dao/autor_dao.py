#import itertools
from database.conexao_factory import ConexaoFactory #new
from model.autor import Autor #new

class AutorDAO:
    #_indice_tabela_autores = itertools.count(start=1)
    #_tabela_autores = []

    def __init__(self):
        self.__conexao_factory = ConexaoFactory() #new

    def get_all(self) -> list[Autor]:
        autores = list()
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, email, telefone, bio FROM lf_livraria.autores")
        resultados = cursor.fetchall()
        for resultado in resultados:
            autor = Autor(resultado[1], resultado[2], resultado[3], resultado[4])
            autor.id = resultado[0]
            autores.append(autor)
        cursor.close()
        conexao.close()
        return autores

    #def get_all(self):
    #    return self._tabela_autores

    def adicionar(self, autor: Autor) -> None:
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO lf_livraria.autores (nome, email, telefone, bio) VALUES (%(nome)s, %(email)s, %(telefone)s, %(biografia)s)",
            ({'nome': autor.nome, 'email': autor.email, 'telefone': autor.telefone, 'biografia': autor.bio}))
        conexao.commit()
        cursor.close()
        conexao.close()

    #def adicionar(self, autor):
    #    autor.id = next(self._indice_tabela_autores)
    #    self._tabela_autores.append(autor)

    #def remover(self, autor_id):
    def remover(self, autor_id: int) -> bool:
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"DELETE FROM lf_livraria.autores WHERE id = {autor_id}")
        autores_removidos = cursor.rowcount
        conexao.commit()
        cursor.close()
        conexao.close()

        if autores_removidos == 0:
            return False
        
        #for index, autor in enumerate(self._tabela_autores):
        #    if autor.id == autor_id:
        #        self._tabela_autores.pop(index)
        #        return True

        return True


    def buscar_por_id(self, autor_id):
        autor = None
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"SELECT id, nome, email, telefone, bio FROM lf_livraria.autores WHERE id = {autor_id}")
        resultado = cursor.fetchone()
        if resultado:
            autor = Autor(resultado[1], resultado[2], resultado[3], resultado[4])
            autor.id = resultado[0]

        cursor.close()
        conexao.close()

        return autor
        #for autor in self._tabela_autores:
        #    if autor.id == autor_id:
        #        return autor

        #return False
