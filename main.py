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

    elif escolha==5:
        fc.cadastrar_cuidados(escolha)

    elif escolha==6:
        fc.sugerir_cuidados(escolha)

    elif escolha==7:
        fc.contar_animais(escolha)

    elif escolha == 8:
        fc.banco_de_dados(escolha)
    
    elif escolha == 9:
<<<<<<< HEAD
        fc.sugerir_adotantes(escolha)
=======
        fc.extra(escolha)
>>>>>>> 1f5de6327833bdf70773b67e0d374edc62db3366





