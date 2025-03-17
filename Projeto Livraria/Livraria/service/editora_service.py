from dao.editora_dao import EditoraDAO
from model.editora import Editora

class EditoraService:
    def __init__(self):
        self._editora_dao: EditoraDAO = EditoraDAO()

    def menu(self):
        print('[Editoras] Escolha uma das seguintes opções:\n'
                '1 - Listar todas as editoras\n'
                '2 - Adicionar nova editora\n'
                '3 - Excluir editora\n'
                '4 - Ver categoria por Id\n'
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
        print('Listando editoras...\n')

        try:
            editoras = self._editora_dao.get_all()
            if editoras:
                for editora in editoras:
                    print(editora)
            else:
                print('Nenhuma editora encontrada!')

        except Exception as e:
            print(f'Erro ao exibir as editoras! - {e}')

    def adicionar(self):
        print('Adicionando editora...\n')

        try:
            nome = input('Digite o nome da editora: ')
            endereco = input('Digite o endereço da editora: ')
            telefone = input('Digite o telefone da editora: ')
            nova_editora = Editora(nome, endereco, telefone)

            self._editora_dao.adicionar(nova_editora)
        except Exception as e:
            print(f'Erro ao inserir editora! - {e}')
        else:
            print('Sucesso! Editora cadastrada.')

    def remover(self):
        print('Removendo editora...\n')

        try:
            editora_id = int(input('Digite o ID da excluir para excluir: '))
            if (self._editora_dao.remover(editora_id)):
                print('Editora excluída com sucesso!')
            else:
                print('Editora não encontrada!')
        except Exception as e:
            print(f'Erro ao excluir editora! - {e}')

    def mostrar_por_id(self):
        print('Editora por Id...\n')

        id = int(input('Digite o Id da editora para buscar: '))
        try:
            edt = self._editora_dao.buscar_por_id(id)
        except Exception as e:
            print(f'Erro ao buscar editora por id! - {e}')
        else:
            if edt:
                print(edt)
            else:
                print('Editora não encontrada!')


    def buscar_por_id(self, editora_id):
        try:
            edt = self._editora_dao.buscar_por_id(editora_id)
        except Exception as e:
            print(f'Erro ao buscar editora por id! - {e}')
        else:
            if edt:
                return edt

        return None
