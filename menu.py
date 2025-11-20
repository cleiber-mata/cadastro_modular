from uteis_limpar_aguardar_pausa import limpar_tela, pausa
from senha_usuario import senha_usuario, colaboradores
from adicionar_listar_item import adicionar_item, listar_itens, estoque_baixo
from grafico_itens_quatidade import grafico_itens_estoque
from lixeira import lixeira_mover, ver_lixeira, restaurar_item, esvaziar_lixeira


def menu_inicial():
    while True:
        print("\nBem vindo ao sistema de gerenciamento de cadastro.")
        print("\n1. Cadastrar Colaborador")
        print("2. Fazer Login")
        print("3. Esqueçi minha senha")
        print("S. Sair")
        
        escolha = input("\nEscolha a opção desejada: ")
        
        if escolha == '1':
            senha_usuario()
        elif escolha == '2':
            usuario_input = input("Digite o usuário: ").strip().lower()
            senha_input = input("Digite a senha: ")
            for colaborador in colaboradores:
                if colaborador["usuario"] == usuario_input and colaborador["senha"] == senha_input:
                    print("Acesso concedido.")
                    pausa(2)
                    limpar_tela()
                    menu()
                    break
            else:
                print("Usuário ou senha incorretos.")
                pausa(2)
                limpar_tela()
        elif escolha == '3':
            print("Por favor, entre em contato com o administrador do sistema para recuperar sua senha.")
            pausa(2)
            limpar_tela()
        elif escolha.lower() == 's':
            print("Saindo do programa.")
            exit()
        else:
            print("Opção inválida. Tente novamente.")
            pausa(2)
            limpar_tela()
            continue
                              
def menu():
    while True:
        print("\nMenu de Opções:")
        print("Escolha a opção desejada ou '9' para SAIR: ")
        print("\n1. Adicionar Item")
        print("2. Listar Itens")
        print("3. Mover Item para Lixeira")
        print("4. Ver Itens Lixeira")
        print("5. Restaurar Item da Lixeira")
        print("6. Esvaziar Lixeira")
        print("7. Grafico de Itens no Estoque")
        print("8. Estoque Baixo Item")
        print("9. Voltar Menu anterior")
        print("S. Sair")
    
        escolha = input("\nOpção: ")
        if escolha == '1':           
            adicionar_item()                     
        elif escolha == '2':
            listar_itens()
        elif escolha == '3':
            lixeira_mover()
        elif escolha == '4':
            ver_lixeira()          
        elif escolha == '5':
            restaurar_item()                     
        elif escolha == '6':
            esvaziar_lixeira()
        elif escolha == '7':
            grafico_itens_estoque()
        elif escolha == '8':
            estoque_baixo()
        elif escolha == '9':
            limpar_tela()
            return               
        elif escolha.lower() == 's':
            print("Obrigado por usar o sistema de gerenciamento de cadastro.")
            print("\n")
            exit()
        else:
            print("Opção inválida. Tente novamente.")