import os
import time

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def aguardar_enter():
    input("\nPressione Enter para continuar...")        
        
def pausa(segundos):
    time.sleep(segundos)