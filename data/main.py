import menu as mn
import funcoes as fc
import os

while True:
    escolha = int(input(mn.MENU_PRINCIPAL))
    if escolha == 1:
        fc.cadastar_animal(escolha)

    elif escolha == 2:
        fc.visualizar_animal(escolha)

    elif escolha==3:
        fc.editar_animal(escolha)

    elif escolha==4:
        fc.excluir_animal(escolha)




