import datetime
from uteis_limpar_aguardar_pausa import limpar_tela, pausa, aguardar_enter
from banco_dados import colaboradores

def senha_usuario():
    print("\n=== Cadastro de novo colaborador ===")
    
    nome = input("Digite o primeiro nome do colaborador: ").strip().lower()
    while nome == "":
        print("O nome não pode ficar em branco.")
        nome = input("Digite o primeiro nome do colaborador: ").strip().lower()
        
    sobrenome = input("Digite o sobrenome do colaborador: ").strip().lower()
    while sobrenome == "":
        print("O sobrenome não pode ficar em branco.")
        sobrenome = input("Digite o sobrenome do colaborador: ").strip().lower()
    usuario = f"{nome}.{sobrenome}"
    
    for colaborador in colaboradores:
        if colaborador["usuario"] == usuario:
            print(f"O login '{usuario}' já existe. Tente outro sobrenome.")
            pausa(2)
            limpar_tela()
            return
        
    senha = input("Digite uma senha numerica de 6 digitos: ")
    while not (senha.isdigit() and len(senha) == 6):
        print("Senha inválida. A senha deve ter exatamente 6 dígitos numericos.")
        senha = input("Digite uma senha numerica de 6 digitos: ")
        
    confirmacao = input("Confirme a senha: ")
    while confirmacao != senha:
        print("As senhas não coincidem. Tente novamente.")
        confirmacao = input("Confirme a senha: ")
    colaborador = {"usuario": usuario, "senha": senha,
                   'data_usuario': datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
    colaboradores.append(colaborador)
    print(f"\nCadastro de colaborador realizado com sucesso! Login: '{usuario}'.")    
    aguardar_enter()
    limpar_tela()
    return