# -*- coding: utf-8 -*-
from menu import menu
from scripts.algoritmo_circular import algoritmo_circular
def main():
    while(True):
        menu()
        opcao = int(input())
        if opcao == 1:
           algoritmo_circular()
        elif opcao == 2:
            pass
        elif opcao == 0:
            print("Saindo...")
            break
        else:
            print("Escolha uma opção válida!")


if __name__ == "__main__":
    main()
