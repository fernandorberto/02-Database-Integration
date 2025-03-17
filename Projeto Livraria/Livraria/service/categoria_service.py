from dao.categoria_dao import CategoriaDAO
from model.categoria import Categoria

class CategoriaService:
    def __init__(self):
        self._categoria_dao: CategoriaDAO = CategoriaDAO()

    def menu(self):
        print('[Categoria] Escolha uma das seguintes opções: \n'
              '1 - Listar todas as categorias\n'
              '2 - Adicionar nova categoria\n'
              '3 - Excluir categoria\n'
              '4 - Ver categoria por ID\n'
              '0 - Voltar ao menu anterior\n')
        escolha = input('Digite a opção: ')

        match escolha:
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
                print('Opção inválida. Por favor, tente novamente!')

        input('\nPressione qualquer tecla para continuar...\n')
        print('*' * 80)
        self.menu()

    def listar(self):
        print('Listando categorias...\n')

        try:
            categorias = self._categoria_dao.get_all()
        except Exception as e:
            print(f'Erro ao exibir os categorias! - {e}')
        else:
            if categorias:
                for categoria in categorias:
                    print(categoria)
            else:
                print('Nenhuma categoria encontrada!')



    def adicionar(self):
        print('Adicionando categoria...\n')
        nome = input('Digite o nome da categoria de livro: ')
        nova_categoria = Categoria(nome)
        try:
            self._categoria_dao.adicionar(nova_categoria)
        except Exception as e:
            print(f'Erro ao adicionar categoria! - {e}')
        else:
            print('Sucesso! Categoria cadastrada.')

    def remover(self):
        print('Removendo categoria...\n')
        categoria_id = int(input('Digite o ID da categoria para excluir: '))
        try:
            if self._categoria_dao.remover(categoria_id):
                print('Categoria excluída com sucesso!')
            else:
                print('Categoria não encontrada!')
        except Exception as ex:
            print(f'Erro ao remover categoria: {ex}')


    def mostrar_por_id(self):
        print('Mostrar categoria por ID...\n')
        categoria_id = int(input('Digite o ID da categoria para buscar: '))
        try:
            cat = self._categoria_dao.buscar_por_id(categoria_id)
        except Exception as ex:
            print(f'Erro ao buscar categoria por id: {ex}')
        else:
            if cat:
                print(cat)
            else:
                print('Categoria não encontrada!')

    def buscar_por_id(self, categoria_id):
        try:
            cat = self._categoria_dao.buscar_por_id(categoria_id)
        except Exception as ex:
            print(f'Erro ao buscar categoria por id: {ex}')
        else:
            if cat:
                return cat

        return None  # reduntante.
