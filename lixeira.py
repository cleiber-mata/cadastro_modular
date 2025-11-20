import datetime
from uteis_limpar_aguardar_pausa import limpar_tela, pausa, aguardar_enter
from banco_dados import estoque, lixeira

def lixeira_mover():
    if not estoque:
        print("Nenhum item cadastrado para mover para a Lixeira.")
        pausa(3)
        limpar_tela()
        return
    try:
        id_lixeira = int(input("Digite o ID do item que deseja mover para a Lixeira: "))
    except ValueError:
        print("Id invalido. Tente novamente.")
        return
    for item in estoque:       
        if item["id"] == id_lixeira:
            item['data_exclusão'] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            lixeira.append(item)
            estoque.remove(item)
            print("\nItem movido para a lixeira com sucesso!")
            pausa(3)
            limpar_tela()
            return
    print(f"O item id {id_lixeira} não cadastrado no estoque ou ja foi removido para a lixeira.")
    pausa(3)
    limpar_tela()
    
    
def ver_lixeira():
        if not lixeira:
            print("Lixeira vazia. Nada para mostrar.")
            pausa(3)
            limpar_tela()
            return
        else:
            limpar_tela()
            print("Itens na Lixeira:")
            print("\nID       Nome         Categoria      Quantidade   Preço         Data/Hora Exclusão")
            print("-"*70)
            for item in lixeira:
                print(f"{item['id']:<8} {item['nome']:<12} {item['categoria']:<14} {item['quantidade']:<12} R$ {item['preco']:<10.2f} {item['data_exclusão']}")
            aguardar_enter()
                
def restaurar_item():
    if not lixeira:
        print("Lixeira vazia. Nenhum item para restaurar.")
        return
    try:
        id_restaurar = int(input("Digite o ID do item que deseja restaurar: "))
    except ValueError:
        print("Id invalido. Tente novamente.")
        pausa(3)
        limpar_tela()
        return
    for item in lixeira:
        if item["id"] == id_restaurar:
            estoque.append(item)
            lixeira.remove(item)
            print("\nItem restaurado com sucesso!")
            pausa(3)
            limpar_tela()
            return
    print(f"O item id {id_restaurar} não encontrado na lixeira.")
    
    
def esvaziar_lixeira():
    if not lixeira:
        print("Lixeira vazia. Nenhum item para excluir.")
        pausa(3)
        limpar_tela()
        return
    else:
        lixeira.clear()
        print("Itens excluidos permanentemente!")
        pausa(3)
        limpar_tela()