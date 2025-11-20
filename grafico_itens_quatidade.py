import matplotlib.pyplot as plt
from adicionar_listar_item import estoque
from uteis_limpar_aguardar_pausa import pausa, limpar_tela

def grafico_itens_estoque():
    if not estoque:
        print("Nenhum item no estoque para gerar o gráfico.")
        pausa(2)
        limpar_tela()
        return
   
    nomes = [item['nome'] for item in estoque]
    quantidades = [item['quantidade'] for item in estoque]
    
    plt.bar(nomes, quantidades, color='blue')
    plt.xlabel('Itens')
    plt.ylabel('Quantidades')
    plt.title('Itens no Estoque')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()