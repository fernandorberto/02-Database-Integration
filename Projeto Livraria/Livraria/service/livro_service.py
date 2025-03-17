from dao.livro_dao import LivroDAO
from dao.categoria_dao import CategoriaDAO
from dao.editora_dao import EditoraDAO
from dao.autor_dao import AutorDAO
from model.livro import Livro

from service.autor_service import AutorService
from service.categoria_service import CategoriaService
from service.editora_service import EditoraService


class LivroService:
    def __init__(self, categoria_dao: CategoriaDAO, editora_dao: EditoraDAO, autor_dao: AutorDAO) -> None:
        self._livro_dao: LivroDAO = LivroDAO()
        self.__categoria_dao: CategoriaDAO = categoria_dao
        self._editora_dao: EditoraDAO = editora_dao
        self._autor_dao: AutorDAO = autor_dao

    #def __init__(self) -> None:
    #    self._livro_dao: LivroDAO = LivroDAO()
    #    self._autor_service = AutorService()
    #    self._categoria_service = CategoriaService()
    #    self._editora_service = EditoraService()

    def menu(self):
        print('[Livros] Escolha uma das seguintes opções:\n'
                '1 - Listar todos os livros\n'
                '2 - Adicionar novo livro\n'
                '3 - Excluir livro\n'
                '4 - Ver livro por Id\n'
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
                print('Opção inválida! Por favor, tente novamente!')

        input('\nPressione qualquer tecla para continuar...\n')
        print('*' * 80)
        self.menu()

    def listar(self):
        print('Listando livros...')

        livros = self._livro_dao.get_all()
        if livros:
            for livro in livros:
                print(livro)
        else:
            print('Nenhum livro encontrado!')

    def adicionar(self):
        print('Adicionando livro...')
        #livro = Livro()
        try:
            titulo = input('Digite o titulo do livro: ')
            resumo = input('Digite o resumo do livro: ')
            ano = int(input('Digite o ano do livro: '))
            paginas = int(input('Digite a quantidade de páginas do livro: '))
            isbn = input('Digite o ISBN do livro: ')

            print('Categorias de livro:')

            lista_categorias = self.__categoria_dao.get_all()
            for cat in lista_categorias:
                print(cat)

            id_categoria = int(input('Digite o ID da categoria do livro: '))
            categoria = self.__categoria_dao.buscar_por_id(id_categoria)

            while categoria is None:
                print('Categoria inexistente!')
                id_categoria = int(input('Digite o ID da categoria do livro: '))
                categoria = self.__categoria_dao.buscar_por_id(id_categoria)

            print('Editoras de livro:')

            lista_editoras = self._editora_dao.get_all()
            for ed in lista_editoras:
                print(ed)

            id_editora = int(input('Digite o ID da editora do livro: '))

            editora = self._editora_dao.buscar_por_id(id_editora)

            while editora is None:
                print('Editora inexistente!')
                id_editora = int(input('Digite o ID da editora do livro: '))
                editora = self._editora_dao.buscar_por_id(id_editora)

            print('Autores de Livro:')

            lista_autores = self._autor_dao.get_all()
            for aut in lista_autores:
                print(aut)

            id_autor = int(input('Digite o ID do autor do livro: '))
            autor = self._autor_dao.buscar_por_id(id_autor)

            while autor is None:
                print('Autor inexistente!')
                id_autor = int(input('Digite o ID do autor do livro: '))
                autor = self._autor_dao.buscar_por_id(id_autor)

            novo_livro = Livro(titulo, resumo, ano, paginas, isbn, categoria, editora, autor)

            self._livro_dao.adicionar(novo_livro)
            print('Livro adicionado com sucesso!')
        except Exception as e:
            print(f'Erro ao inserir novo livro: {e}')

        input('\nPressione uma tecla para continuar...\n')

        #livro.titulo = input('Digite o título do livro: ')
        #livro.resumo = input('Digite o resumo do livro: ')
        #livro.ano = int(input('Digite o ano do livro: '))
        #livro.paginas = int(input('Digite a quantidade de páginas do livro: '))
        #livro.isbn = input('Digite o ISBN do livro: ')

        #print('Autores disponíveis:')

        #self._autor_service.listar()

        #id_autor = int(input('Digite o ID do autor do livro: '))

        #livro.autor = self._autor_service.buscar_por_id(id_autor)

        #print('Categorias disponíveis:')
        #self._categoria_service.listar()

        #id_categoria = int(input('Digite o ID da categoria do livro: '))
        #livro.categoria = self._categoria_service.buscar_por_id(id_categoria)

        #print('Editoras disponíveis:')
        #self._editora_service.listar()

        #id_editora = int(input('Digite o ID da editora do livro: '))
        #livro.editora = self._editora_service.buscar_por_id(id_editora)

        #try:
        #    self._livro_dao.adicionar(livro)
        #except Exception as e:
        #    print(f'Erro ao adicionar livro: {e}')

    def remover(self):
        print('Removendo livro...')
        livro_id = int(input('Digite o ID do livro para excluir: '))
        try:
            if self._livro_dao.remover(livro_id):
                print('Livro excluído com sucesso!')
            else:
                print('Livro não encontrado!')
        except Exception as ex:
            print(f'Erro ao remover livro: {ex}')

    def mostrar_por_id(self):
        print('Livro por Id...\n')

        id = int(input('Digite o Id do livro para buscar: '))
        try:
            livro = self._livro_dao.buscar_por_id(id)
        except Exception as e:
            print(f'Erro ao buscar livro por id: {e}')
        else:
            if livro:
                print(livro)
            else:
                print('Livro não encontrado!')

