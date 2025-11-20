import datetime
from uteis_limpar_aguardar_pausa import limpar_tela, pausa, aguardar_enter
from banco_dados import estoque

def adicionar_item():
    global proximo_id
    
    nome = input(f"Digite o nome do item: ").strip().lower()
    categoria = input("Digite a categoria do item: ").strip().lower()
    quantidade_str = input("Digite a quantidade do item: ").strip()
    preco_str = input("Digite o preço do item: ").strip()
    
    # Verifica campos vazios
    if not nome or not categoria or not quantidade_str or not preco_str:
        print("\nErro: Nenhum campo pode ficar vazio!")
        pausa(2)
        limpar_tela()
        return

    # Validação de número
    if not quantidade_str.isdigit():
        print("\nErro: Quantidade inválida!")
        pausa(2)
        limpar_tela()
        return
    try:
        preco = float(preco_str)
    except:
        print("\nErro: Preço inválido!")
        pausa(2)
        limpar_tela()
        return

    quantidade = int(quantidade_str)
    
    item = {
        'id': proximo_id,
        'nome': nome,
        'categoria': categoria,
        'quantidade': quantidade,
        'preco': preco,
        "estoque_baixo" : quantidade <= 5,
        'data_cadastro': datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
    
    estoque.append(item)
    proximo_id += 1
    print("\nItem adicionado com sucesso!")
    print("Cadastro: ", proximo_id-1)
    aguardar_enter()
    limpar_tela()
    
    
def listar_itens():
    if not estoque:
        print("Nenhum item cadastrado.")
        pausa(3)
        return
    limpar_tela()
    print("Itens do Estoque.")
    print("\nID       Nome         Categoria      Quantidade   Preço         Data/Hora Cadastro")
    print("-"*70)
    for item in estoque:
        print(f"{item['id']:<8} {item['nome']:<12} {item['categoria']:<14} {item['quantidade']:<12} R$ {item['preco']:<10.2f} {item['data_cadastro']}")
    aguardar_enter()
    
def estoque_baixo():
    itens_baixo_estoque = [item for item in estoque if item['estoque_baixo']]
    if not itens_baixo_estoque:
        print("Nenhum item com estoque baixo.")
        pausa(2)
        limpar_tela()
        return
    limpar_tela()
    print("Itens com Estoque Baixo (menos de 5 unidades):")
    print("\nID       Nome         Categoria      Quantidade   Preço         Data/Hora Cadastro")
    print("-"*70)
    for item in itens_baixo_estoque:
        print(f"{item['id']:<8} {item['nome']:<12} {item['categoria']:<14} {item['quantidade']:<12} R$ {item['preco']:<10.2f} {item['data_cadastro']}")
    aguardar_enter()
