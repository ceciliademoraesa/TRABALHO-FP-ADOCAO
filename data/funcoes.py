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
                print(f"  NOME: {campo[1]}")
                print(f"  IDADE: {campo[2]}")
                print(f"  ESPECIE: {campo[3]}")
                print(f"  RAÇA: {campo[4]}")
                print(f"  DATA DE CHEGADA: {campo[5]}")
                print(f"  ESTADO DE SAÚDE: {campo[6]}")

        if animal_encontrado == 0: 
            os.system("cls")
            print("\nId inválido.")


def editar_animal(escolha):
    if escolha == 3:
        os.system("cls")

        id_edicao = input("Escolha o ID de orçamento que deseja atualizar: ")

        with open("data/animais.csv", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        encontrado = False
        linhas_novas = []

        def pedir_float_enter(mensagem, atual):
            while True:
                entrada = input(mensagem)

                if entrada == "":
                    return atual

                try:
                    return str(float(entrada))

                except ValueError:
                    print("\nInforme um valor numérico válido!")

        for linha in linhas:
            campos = linha.strip().split(",")

            if campos[0] == "id_orcamento":
                linhas_novas.append(linha)
                continue

            if campos[0] == id_edicao:
                encontrado = True

                print(f"\Animal {id_edicao} encontrado!")
                print("Para manter o valor atual, deixe o campo em branco.\n")

                nome = input(f"Nome [{campos[1]}]: ").lower() or campos[1]
                idade = input(f"Idade [{campos[2]}]: ").lower() or campos[2]
                especie = input(f"Espécie [{campos[3]}]: ").lower() or campos[2]
                raca = input(f"Raca[{campos[3]}]: ").lower() or campos[3]
                data_de_chegada = pedir_float_enter(f"Data de chegada [{campos[4]}]: ",campos[4])
                estado_de_saude = pedir_float_enter(f"Estado de saúde [{campos[5]}]: ",campos[5])
                

                nova_linha = (f"{id_edicao},{nome},{idade},{especie},{raca},{data_de_chegada}\n")
                linhas_novas.append(nova_linha)

            else:
                linhas_novas.append(linha)

        if not encontrado:
            print("ID não encontrado.")
            return

        # Reescreve arquivo
        with open("data/animais.csv", "w", encoding="utf-8") as arquivo:
            arquivo.writelines(linhas_novas)

        print(f"Animal {id_edicao} atualizado com sucesso!")

def excluir_animal(escolha):
    if escolha == 4:
        os.system("cls")

        id_excluir = input("Informe o ID do orçamento que deseja deletar: ")

        with open("data/animais.csv", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        encontrado = False
        linhas_novas = []

        for linha in linhas:
            campos = linha.strip().split(",")

            if campos[0] == "id_animal":
                linhas_novas.append(linha)
                continue

            if campos[0] == id_excluir:
                encontrado = True
                confirmacao = input(f"\nTem certeza que deseja deletar o animal {id_excluir}? (s/n): ").lower()
                if confirmacao != "s":
                    print("\nOperação cancelada.")
                    return
            else:
                linhas_novas.append(linha)

        if not encontrado:
            print("ID não encontrado.")
            return

        with open("data/animais.csv", "w", encoding="utf-8") as arquivo:
            arquivo.writelines(linhas_novas)

        print(f"Animal {id_excluir} deletado com sucesso!")

        


       