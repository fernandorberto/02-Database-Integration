from service.autor_service import AutorService
from service.categoria_service import CategoriaService
from service.editora_service import EditoraService
from service.livro_service import LivroService

autor_service = AutorService()
categoria_service = CategoriaService()
editora_service = EditoraService()
#livro_service = LivroService()
livro_service = LivroService(categoria_service._categoria_dao, editora_service._editora_dao, autor_service._autor_dao)

while True:
    print('[Menu Principal] Escolha uma das seguintes opções:\n'
            '1 - Categorias\n'
            '2 - Editoras\n'
            '3 - Autores\n'
            '4 - Livros\n'
            '0 - Sair do programa\n')
    escolha_main = input('Digite a opção: ')

    match escolha_main:
        case '0':
            break
        case '1':
            categoria_service.menu()
        case '2':
            editora_service.menu()
        case '3':
            autor_service.menu()
        case '4':
            livro_service.menu()
        case _:  # default
            print('Opção inválida!')

    print('*' * 80)
