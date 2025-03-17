from model.autor import Autor
from dao.autor_dao import AutorDAO
# Banco de dados

class AutorService:
    def __init__(self):
        self._autor_dao = AutorDAO()
        #self._autor_dao: AutorDAO = AutorDAO()

    @property
    def autor_dao(self) -> AutorDAO:
        return self.__autor_dao

    def menu(self):
        print('[Autores] Escolha uma das seguintes opções:\n'
                '1 - Listar autores\n'
                '2 - Adicionar autor\n'
                '3 - Excluir autor\n'
                '4 - Ver autor por Id\n'
                '0 - Voltar ao menu anterior\n')
        escolha_aut = input('Digite a opção: ')

        match escolha_aut:
            case '0':
                return
            case '1':
                self.listar()
            case '2':
                self.adicionar()
            case '3':
                self.remover()
            case '4':
                self.mostrar_por_id()
            case _:
                print('Opção inválida!')

        input('\nPressione qualquer tecla para continuar...\n')
        print('*' * 80)
        self.menu()

    def listar(self):
        print('Listando autores...\n')

        try:
            autores = self._autor_dao.get_all()
        except Exception as ex:
            print(f'Ocorreu um erro ao buscar autores: {ex}')
        else:
            if autores:
                for autor in autores:
                    print(autor)
            else:
                print('Nenhum autor cadastrado!')

    def adicionar(self):
        print('Adicionando autor... \n')

        #autor = Autor()

        try:
            nome = input('Digite o nome do autor: ')
            email = input('Digite o email do autor: ')
            telefone = input('Digite o telefone do autor: ')
            bio = input('Digite uma bio reduzida do autor: ')
            novo_autor = Autor(nome, email, telefone, bio)
            self._autor_dao.adicionar(novo_autor)
            print('Autor adicionado com sucesso!')
        except Exception as e:
            print(f'Erro ao inserir autor! - {e}')
            return

        #autor.nome = input('Digite o nome do autor: ')
        #autor.email = input('Digite o email: ')
        #while True:
        #    try:
        #        # autor.telefone = input('Digite o telefone: ')
        #        autor.telefone = '+551191234-5678'
        #    except:
        #        print('Número de telefone inválido. Tente novamente')
        #    else:  # Se não ocorreu exceção de telefone inválido, então:
        #        break

        #autor.bio = input('Digite a minibiografia: ')

        #try:
        #    self._autor_dao.adicionar(autor)
        #except Exception as ex:
        #    print(f'Ocorre um erro ao adicionar autor: {ex}')
        #else:
        #    print('Sucesso! Autor cadastrado.')

    def remover(self):
        print('Removendo autor...\n')

        autor_id = int(input('Digite o ID do autor a ser excluído: '))
        try:
            if self._autor_dao.remover(autor_id):
                print('Autor excluído com sucesso!')
            else:
                print('ID do autor não encontrado.')
        except Exception as ex:
            print(f'Erro ao remover o autor: {ex}')

    def mostrar_por_id(self):
        print('Mostrando um único autor...\n')
        autor_id = int(input('Digite o ID do autor a ser buscado: '))

        try:
            autor = self._autor_dao.buscar_por_id(autor_id)
        except Exception as ex:
            print(f'Ocorreu um erro ao buscar autor por id: {ex}')
        else:
            if autor:
                print(autor)
                return autor
            else:
                print('Autor não encontrado!')

    def buscar_por_id(self, autor_id):
        try:
            autor = self._autor_dao.buscar_por_id(autor_id)
        except Exception as ex:
            print(f'Ocorreu um erro ao buscar autor por id: {ex}')
        else:
            if autor:
                return autor

        return None
