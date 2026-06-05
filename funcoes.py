from datetime import datetime
import os

def gerar_id(arquivo):
    if not os.path.exists(arquivo):
        return 1
    with open(arquivo, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        return len(linhas)
            
def cadastar_animal(escolha):
    if escolha == 1:
        os.system("cls")

        nome = input("INFORME O NOME DO ANIMAL: ").lower()
        idade = input("INFORME A IDADE DO ANIMAL: ").lower()
        especie = input("INFORME A ESPÉCIE DO ANIMAL: ").lower()
        raca = input("INFORME A RAÇA DO ANIMAL: ").lower()
        opcao_data = int(input("DIGITE [1] PARA CADASTRAR A DATA MANUALMENTE OU [2] PARA USAR A DATA ATUAL: "))
        
        if opcao_data == 1:
            data_de_chegada = input("INFORME A DATA DE CHEGADA: ")
        elif opcao_data == 2:
            data_de_chegada = datetime.now().strftime("%d/%m/%Y")
        
        print("ESTADO DE SAÚDE")
        print("1 - BOM")
        print("2 - ESTÁVEL")
        print("3 - RUIM")
        estado_de_saude = int(input("SELECIONE O ESTADO DE SAÚDE DO ANIMAL: "))

        id_animal = gerar_id("data/animais.csv")
        print(f"O ID DO ANIMAL É: {id_animal}")

        arquivo_existente = os.path.exists("data/animais.csv")

        with open("data/animais.csv", "a", newline="", encoding="utf-8") as arquivo:
            if not arquivo_existente:
                arquivo.write("id_animal,nome,idade,especie,raca,data_de_chegada,estado_de_saude\n")

                arquivo.write(f"{id_animal},{nome},{idade},{especie},{raca},{data_de_chegada},{estado_de_saude}\n")

        print("ANIMAL CADASTRADO COM SUCESSO!")

def visualizar_animal(escolha):
    if escolha == 2:
        os.system("cls")
        id_verificacao_animal = input("INFORME O ID DO ANIMAL QUE DESEJA VISUALIZAR: ")

        with open("data/animais.csv", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        animal_encontrado = 0

        for linha in linhas:
            campo = linha.split(",")
            if id_verificacao_animal == campo[0]:
                animal_encontrado += 1 
                print(f"  NOME: {campo[1]}")
                print(f"  IDADE: {campo[2]}")
                print(f"  ESPÉCIE: {campo[3]}")
                print(f"  RAÇA: {campo[4]}")
                print(f"  DATA DE CHEGADA: {campo[5]}")
                print(f"  ESTADO DE SAÚDE: {campo[6]}")

        if animal_encontrado == 0: 
            os.system("cls")
            print("\nID INVÁLIDO.")

def editar_animal(escolha):
    if escolha == 3:
        os.system("cls")

        id_edicao = input("ESCOLHA O ID DE ORÇAMENTO QUE DESEJA ATUALIZAR: ")

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
                    print("\nINFORME UM VALOR NUMÉRICO VÁLIDO!")

        for linha in linhas:
            campos = linha.strip().split(",")

            if campos[0] == "id_orcamento":
                linhas_novas.append(linha)
                continue

            if campos[0] == id_edicao:
                encontrado = True

                print(f"\ANIMAL {id_edicao} ENCONTRADO!")
                print("PARA MANTER O VALOR ATUAL, DEIXE O CAMPO EM BRANCO.\n")

                nome = input(f"NOME [{campos[1]}]: ").lower() or campos[1]
                idade = input(f"IDADE [{campos[2]}]: ").lower() or campos[2]
                especie = input(f"ESPÉCIE [{campos[3]}]: ").lower() or campos[2]
                raca = input(f"RAÇA [{campos[3]}]: ").lower() or campos[3]
                data_de_chegada = pedir_float_enter(f"DATA DE CHEGADA [{campos[4]}]: ",campos[4])
                estado_de_saude = pedir_float_enter(f"ESTADO DE SAÚDE [{campos[5]}]: ",campos[5])
                
                nova_linha = (f"{id_edicao},{nome},{idade},{especie},{raca},{data_de_chegada}\n")
                linhas_novas.append(nova_linha)

            else:
                linhas_novas.append(linha)

        if not encontrado:
            print("ID NÃO ENCONTRADO.")
            return

        with open("data/animais.csv", "w", encoding="utf-8") as arquivo:
            arquivo.writelines(linhas_novas)

        print(f"ANIMAL {id_edicao} ATUALIZADO COM SUCESSO!")

def excluir_animal(escolha):
    if escolha == 4:
        os.system("cls")

        id_excluir = input("INFORME O ID DO ORÇAMENTO QUE DESEJA DELETAR: ")

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
                confirmacao = input(f"\nTEM CERTEZA QUE DESEJA DELETAR O ANIMAL {id_excluir}? (S/N): ").lower()
                if confirmacao != "s":
                    print("\nOPERAÇÃO CANCELADA.")
                    return
            else:
                linhas_novas.append(linha)

        if not encontrado:
            print("ID NÃO ENCONTRADO.")
            return

        with open("data/animais.csv", "w", encoding="utf-8") as arquivo:
            arquivo.writelines(linhas_novas)

        print(f"ANIMAL {id_excluir} DELETADO COM SUCESSO!")

def cadastrar_cuidados(escolha):
    if escolha == 5:
        os.system("cls")

        id_animal = input("INFORME O ID DO ANIMAL: ")

        id_cadastrado = gerar_id("data/animais.csv") - 1

        if int(id_animal) > id_cadastrado:
            print("ID INVÁLIDO! ANIMAL NÃO ENCONTRADO.")
            return

        print("\nTIPO DE CUIDADO")
        print("1 - VACINA")
        print("2 - BANHO")
        print("3 - CONSULTA VETERINÁRIA")
        print("4 - TREINO")
        print("5 - OUTRO")
        opcao_tipo = int(input("\nSELECIONE O TIPO DE CUIDADO: "))

        if opcao_tipo == 1:
            tipo_de_cuidado = "vacina"
        elif opcao_tipo == 2:
            tipo_de_cuidado = "banho"
        elif opcao_tipo == 3:
            tipo_de_cuidado = "consulta veterinaria"
        elif opcao_tipo == 4:
            tipo_de_cuidado = "treino"
        elif opcao_tipo == 5:
            tipo_de_cuidado = input("DESCREVA O TIPO DE TAREFA: ").lower()

        descricao = input("DESCRIÇÃO DA ATIVIDADE: ").lower()
        responsavel = input("RESPONSÁVEL PELA ATIVIDADE: ").lower()

        opcao_data = int(input("DIGITE [1] PARA INFORMAR A DATA PREVISTA OU [2] PARA USAR A DATA ATUAL: "))
        if opcao_data == 1:
            data_prevista = input("INFORME A DATA PREVISTA (dd/mm/aaaa): ")
        elif opcao_data == 2:
            data_prevista = datetime.now().strftime("%d/%m/%Y")

        id_cuidado = gerar_id("data/cuidados.csv")

        arquivo_existente = os.path.exists("data/cuidados.csv")

        with open("data/cuidados.csv", "a", newline="", encoding="utf-8") as arquivo:
            if not arquivo_existente:
                arquivo.write("id_tarefa,id_animal,tipo,descricao,responsavel,data_prevista\n")
            arquivo.write(f"{id_cuidado},{id_animal},{tipo_de_cuidado},{descricao},{responsavel},{data_prevista}\n")

        print("TAREFA CADASTRADA COM SUCESSO.")

animais = [] 

def data_hoje():
    return datetime.date.today()
 
def formatar_data(data_str):
    try:
        return datetime.datetime.strptime(data_str, "%d/%m/%Y").date()
    except ValueError:
        return None

def buscar_animal_por_id(id_buscado):
    for a in animais:
        if a[0] == id_buscado:
            return a
    return None

def sugerir_cuidados(escolha):
    if escolha == 6:
        os.system("cls")
        print("\nSUGESTÕES DE CUIDADOS")
        
        if len(animais) == 0:
            print("NENHUM ANIMAL CADASTRADO.")
            return
        
        print("\nANIMAIS DISPONÍVEIS: ")
        for a in animais:
            print(f"    #{a[0]} – {a[1]} ({a[2]})")

        try:
            id_buscado = int(input("\n  ID DO ANIMAL: "))
        except ValueError:
            print("ID INVÁLIDO!")
            return
        
        animal = buscar_animal_por_id(id_buscado)
        if animal is None:
            print("ANIMAL NÃO ENCONTRADO!")
            return
        
        nome = animal[1]
        especie = animal[2].lower()
        idade = animal[4]
        
        try:
            idade = int(idade)

        except (ValueError, TypeError):
            idade = 0
            
        print(f"\nSUGESTÕES PARA {nome.upper()} ({especie}):\n")
            
        if especie == "cão" or especie == "cao":
            print("BANHO E TOSA A CADA 30 DIAS.")
            print("PASSEIOS DIÁRIOS DE PELO MENOS 30 MINUTOS.")
            print("VERMIFUGAÇÃO A CADA 3 MESES.")
            print("VACINAS: V10 ANUAL E ANTIRRÁBICA ANUAL.")
            
        elif especie == "gato":
            print("\nCAIXA DE AREIA LIMPA DIARIAMENTE.")
            print("ARRANHADORES E BRINQUEDOS.")
            print("VACINAS: V4 FELINA ANUAL E ANTIRRÁBICA ANUAL.")
            print("VERMIFUGAÇÃO A CADA 3 MESES.")

        else:
            print("\nCONSULTE UM VETERINÁRIO ESPECIALISTA NA ESPÉCIE.")
            print("VERIFIQUE NECESSIDADES ESPECÍFICAS DE DIETA E ESPAÇO.")

        if idade <= 1:
            print("\nFILHOTE: MANTER VACINAS E FERMIFUGAÇÃO EM DIA.")
            print("ALIMENTAÇÃO ESPECÍFICA PARA FILHOTES.")
            print("SOCIALIZAÇÃO PRECOCE É FUNDAMENTAL.")
            
        elif idade >= 8:
            print("\nSÊNIOR: CHECK-UP VETERINÁRIO A CADA 6 MESES.")
            print("ATENÇÃO A ARTICULAÇÕES E PESO. ")
            print("DIETA ADAPTADA PARA A IDADE. ")
            
        try:
            saude = int(animal[6])
        except (ValueError, TypeError, IndexError):
            saude = 0
        
        if saude == 2:
            print("\nESTADO ESTÁVEL: MONITORAR DE PERTO E AGENDAR CONSULTA!")
        elif saude == 3:
            print("\nESTADO RUIM: ENCAMINHAR AO VETERINÁRIO COM URGÊNCIA!")

def calcular_compatibilidade(animal, adotante):
    pontos = 0
    
    especie = animal[2].lower().strip()
    try:
        idade = int(animal[4])
    
    except (ValueError, TypeError):
        idade = 0

    try:
        saude = int(animal[6])
    except (ValueError, TypeError, IndexError):
        saude = 1

    pref_especie = adotante["preferencia_especie"].lower().strip()
    if pref_especie == "qualquer" or pref_especie == especie:
       pontos += 30
 
    if adotante["quintal"] and (especie == "cão" or especie == "cao"):
       pontos += 20
    elif not adotante["quintal"] and especie == "gato":
        pontos += 20
    else:
       pontos += 10
    if adotante["criancas"] and idade <= 3:
       pontos += 20
    elif not adotante["criancas"]:
       pontos += 20
 
    if adotante["experiencia"] and saude == 3:
       pontos += 30
    elif adotante["experiencia"]:
       pontos += 20
    elif saude < 3:
       pontos += 10
    
    return min(pontos, 100)

def sugerir_adotantes(escolha):
    if escolha == 9:
        print("\nSUGESTÕES DE ADOTANTES COMPATÍVEIS")

        with open("data/animais.csv", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        print("\nANIMAIS DISPONÍVEIS:")
        for linha in linhas:
            if linha.startswith("id_animal") or not linha.strip():
                continue
            campos = linha.strip().split(",")
            print(f"  #{campos[0]} - {campos[1]} ({campos[2]})")

        id_buscado = input("\nID DO ANIMAL: ").strip()

        animal = None
        for linha in linhas:
            campos = linha.strip().split(",")
            if campos[0] == id_buscado:
                animal = campos
                break

        if animal is None:
            print("ANIMAL NÃO ENCONTRADO.")
            return

        print(f"\nPERFIL DO ADOTANTE PARA {animal[1].upper()}\n")
        nome  = input("NOME DO ADOTANTE: ").strip()
        pref = input("PREFERÊNCIA DE ESPÉCIE (cão/gato/outro): ").strip().lower()
        quintal = input("TEM QUINTAL? (s/n): ").strip().lower() == "s"
        criancas = input("TEM CRIANÇAS EM CASA? (s/n): ").strip().lower() == "s"
        experiencia = input("TEM EXPERIÊNCIA COM PETS? (s/n): ").strip().lower() == "s"

        adotante = {
            "nome": nome,
            "preferencia_especie": pref,
            "quintal": quintal,
            "criancas": criancas,
            "experiencia": experiencia
        }

        score = calcular_compatibilidade(animal, adotante)
        barra = "█" * (score // 10) + "░" * (10 - score // 10)

        print(f"\nCOMPATIBILIDADE DE {nome} COM {animal[1].upper()}:")
        print(f"  [{barra}] {score}%")

        if score >= 70:
            print("ÓTIMO. RECOMENDADO PARA ADOÇÃO.")
        elif score >= 40:
            print("MÉDIO. VALE UMA CONVERSA.")
        else:
            print("BAIXA. CONSIDERE OUTRO ANIMAL.")

def mostrar_cuidados_animais(id_animal):
    if not os.path.exists("data/cuidados.csv"):
        print("\nNENHUM CUIDADO CADASTRADO.")
        return

    with open("data/cuidados.csv", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    print("\nPRÓXIMOS CUIDADOS:")
    encontrou = 0

    for linha in linhas:
        if linha.startswith("id_cuidado"):
            continue
        if not linha.strip():        
            continue

        campos = linha.strip().split(",")

        if campos[1].strip() != id_animal:
            continue
        if campos[5].strip() == "s":
            continue

        encontrou += 1
        tipo = campos[2].strip()
        data_prevista = campos[4].strip()
        hoje = datetime.now().date()
        data = datetime.strptime(data_prevista, "%d/%m/%Y").date() 

        dias = (data - hoje).days

        if dias < 0:
            situacao = f"ATRASADA {abs(dias)} DIA(S)!"
        elif dias == 0:
            situacao = "HOJE!"
        elif dias == 1:
            situacao = "AMANHÃ!"
        else:
            situacao = f"FALTAM {dias} DIA(S)"

        print(f"TIPO: {tipo}")
        print(f"DATA: {data_prevista}")
        print(f"STATUS: {situacao}")

    if encontrou == 0:
        print("NENHUM CUIDADO PENDENTE.")

def contar_animais(escolha):
   if escolha == 7:
        os.system("cls")
                
        if not os.path.exists("data/animais.csv"):
            print("NENHUM ANIMAL CADASTRADO.")
            return

        with open("data/animais.csv", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        total = 0
        bom = 0
        estavel = 0
        ruim = 0
        filhote = 0
        adulto = 0
        idoso = 0

        for linha in linhas:
            if linha.startswith("id_animal"):
                continue

            campos = linha.strip().split(",")
            total += 1

            saude = campos[6].strip()
            if saude == "1":
                bom += 1
            elif saude == "2":
                estavel += 1
            elif saude == "3":
                ruim += 1

            idade = int(campos[2].strip())
            if idade <= 2:
                filhote += 1
            elif idade <= 6:
                adulto += 1
            else:
                idoso += 1

        print(f"TOTAL DE ANIMAIS: {total}")

        print("\nESTADO DE SAÚDE:")
        print(f"BOM: {bom} ANIMAIS")
        print(f"ESTÁVEL: {estavel} ANIMAIS")
        print(f"RUIM: {ruim} ANIMAIS")

        print("\nFAIXA ETÁRIA:")
        print(f"FILHOTE (ATÉ 2 ANOS):  {filhote} ANIMAIS")
        print(f"ADULTO (3 A 6 ANOS):  {adulto} ANIMAIS")
        print(f"IDOSO (ACIMA DE 6):  {idoso} ANIMAIS")

        print("\nPORCENTAGEM POR SAÚDE:")
        if total > 0:
            print(f"BOM:     {bom / total * 100:.1f}%")
            print(f"ESTÁVEL: {estavel / total * 100:.1f}%")
            print(f"RUIM:    {ruim / total * 100:.1f}%")

        print("\nPORCENTAGEM POR IDADE:")
        if total > 0:
            print(f"FILHOTE: {filhote / total * 100:.1f}%")
            print(f"ADULTO:  {adulto / total * 100:.1f}%")
            print(f"IDOSO:   {idoso / total * 100:.1f}%")

def banco_de_dados(escolha):
    if escolha == 8:
        os.system("cls")

        total_de_animais = gerar_id("data/animais.csv") - 1
        total_de_cuidados = gerar_id("data/cuidados.csv") - 1

        print("BANCO DE DADOS")
        print(f"\nTOTAL DE ANIMAIS: {total_de_animais}")
        print(f"TOTAL DE CUIDADOS: {total_de_cuidados}")
        print("\nTAREFAS:")

        with open("data/cuidados.csv", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        for linha in linhas:
            if linha.startswith("id_cuidado"):
                continue

            campos = linha.strip().split(",") 

            print(f"\nTAREFAS {campos[0]}")
            print(f"Animal ID: {campos[1]}")
            print(f"Tipo: {campos[2]}")
            print(f"Descrição: {campos[3]}")
            print(f"Responsável: {campos[4]}")
            print(f"Data prevista: {campos[5]}")

        print("==================================")

def extra(escolha):
    if escolha == 9:
        escolha