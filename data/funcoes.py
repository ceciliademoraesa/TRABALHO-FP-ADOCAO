from datetime import datetime
import os

def gerar_id():
            if not os.path.exists("data/animais.csv"): 
                return 1 
            
            with open("data/animais.csv", "r", encoding="utf-8") as arquivo: 
                linhas = arquivo.readlines() 
                return len(linhas)
            
def cadastar_animal(escolha):
    if escolha == 1:
        nome = input("Informe o nome do animal: ").lower()
        idade = input("Infome a idade do animal: ").lower()
        especie = input("Informe a especie do animal: ").lower()
        raca = input("Informe a raça do animal: ").lower()
        opcao_data = int(input("Digite [1] para cadastrar a data manualmente ou [2] para usar a data atual: "))
        
        if opcao_data == 1:
            data_de_chegada = input("Informe a data de chegada: ")
        elif opcao_data == 2:
            data_de_chegada = datetime.now().strftime("%d/%m/%Y")
        
        print("Estado de saúde")
        print("1 - BOM")
        print("2- ESTAVEL")
        print("3 - RUIM")
        estado_de_saude = int(input("Selecione o estado de saúde do animal: "))

        id_animal = gerar_id()
        print(f"O ID do animal é: {id_animal}")

        arquivo_existente = os.path.exists("data/animais.csv")

        with open("data/animais.csv", "a", newline="", encoding= "utf-8") as arquivo:
            if not arquivo_existente:
                  arquivo.write("id_animal,nome,idade,especie,raca,data_de_chegada,estado_de_saude")
            arquivo.write(f"{id_animal}, {nome}, {idade}, {especie}, {raca}, {data_de_chegada}, {estado_de_saude}")

        print("ANIMAL CADRASTADO COM SUCESSO!")

def visualizar_animal(escolha):
    if escolha == 2:
        os.system("cls")
        id_verificacao_animal = input("Informe o ID do animal que deseja visualizar: ")

        with open("data/animais.csv", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        animal_encontrado = 0

        for linha in linhas:
            campo = linha.split(",")
            if id_verificacao_animal == campo[0]:
                animal_encontrado += 1 
                print(f"  NOME: {campo[0]}")
                print(f"  IDADE: {campo[1]}")
                print(f"  ESPECIE: {campo[2]}")
                print(f"  RAÇA: {campo[3]}")
                print(f"  DATA DE CHEGADA: {campo[4]}")
                print(f"  ESTADO DE SAÚDE: {campo[5]}")

        if animal_encontrado == 0: 
            os.system("cls")
            print("\nId inválido.")
        


       