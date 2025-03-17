#import itertools
from database.conexao_factory import ConexaoFactory
from model.editora import Editora

class EditoraDAO:
    #_id_editora = itertools.count(start=1)
    #_tabela_editoras: list[Editora] = list()

    def __init__(self):
        self.__conexao_factory = ConexaoFactory()

    #    pass

    def get_all(self) -> list[Editora]:
        editoras = list()
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, endereco, telefone FROM lf_livraria.editoras")
        resultados = cursor.fetchall()
        for resultado in resultados:
            editora = Editora(resultado[1], resultado[2], resultado[3])
            editora.id = resultado[0]
            editoras.append(editora)
        cursor.close()
        conexao.close()
        return editoras
    #    return self._tabela_editoras

    def adicionar(self, editora: Editora) -> None:
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO lf_livraria.editoras (nome, endereco, telefone) VALUES (%(nome)s, %(endereco)s, %(telefone)s)",
            ({'nome': editora.nome, 'endereco': editora.endereco, 'telefone': editora.telefone}))
        conexao.commit()
        cursor.close()
        conexao.close()

        #editora.id = next(self._id_editora)
        #self._tabela_editoras.append(editora)

    def remover(self, editora_id: int) -> bool:
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"DELETE FROM lf_livraria.editoras WHERE id = {editora_id}")
        editoras_removidas = cursor.rowcount
        conexao.commit()
        cursor.close()
        conexao.close()

        if editoras_removidas == 0:
            return False

        return True
    
        #for editora in self._tabela_editoras:
        #    if (editora.id == editora_id):
        #        index = self._tabela_editoras.index(editora)
        #        self._tabela_editoras.pop(index)
        #        return True

        #return False

    def buscar_por_id(self, editora_id) -> bool | Editora:
        editora = None
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"SELECT id, nome, endereco, telefone FROM lf_livraria.editoras WHERE id = {editora_id}")
        resultado = cursor.fetchone()
        if resultado:
            editora = Editora(resultado[1], resultado[2], resultado[3])
            editora.id = resultado[0]

        cursor.close()
        conexao.close()

        return editora
    
        #for editora in self._tabela_editoras:
        #    if (editora.id == editora_id):
        #        return editora

        #return False
