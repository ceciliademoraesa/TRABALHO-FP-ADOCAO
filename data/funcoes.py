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

animais = [] 
tarefas = [] 

def data_hoje():
    return datetime.date.today()
 
def formatar_data(data_str):
    try:
        return datetime.datetime.strptime(data_str, "%d/%m/%Y").date()
    except ValueError:
        return None

def status_tarefa(t):
    hoje = data_hoje()
    if t[5] == "Concluída":
        return "Tarefa concluída"
    elif t[3] < hoje:
        return "Tarefa atrasada"
    else:
        return "Tarefa pendente"


def buscar_animal_por_id(id_buscado):
    for a in animais:
        if a[0] == id_buscado:
            return a
    return None


def criar_tarefa():
    print("  \nCRIAR TAREFA / CUIDADO")
    if len(animais) == 0:
        print("\n Cadastre um animal primeiro!")
        return

    print("\nAnimais disponíveis:")
    for a in animais:
        print(f"    #{a[0]} – {a[1]} ({a[2]})")

    
    try:
        id_animal = int(input("  ID do animal    : "))
    except ValueError:
        print(" ID inválido!")
        return

    animal = buscar_animal_por_id(id_animal)
    if animal is None:
        print(" Animal não encontrado!")
        return

    print(f"\n  Animal: {animal[1]}")
    print()
    print("  Tipos de cuidado:")
    print("  1 – Vacina          2 – Banho")
    print("  3 – Consulta Vet.   4 – Treino")
    print("  5 – Vermifugação    6 – Outro")

    opcao_tipo = input("\n  Escolha o tipo (1-6): ").strip()
    tipos = {
        "1": "Vacina", "2": "Banho", "3": "Consulta Vet.",
        "4": "Treino", "5": "Vermifugação", "6": "Outro"
    }

    if opcao_tipo not in tipos:
        print(" Opção inválida!")
        return

    tipo = tipos[opcao_tipo]

    data_str  = input("  Data prevista (DD/MM/AAAA): ").strip()
    data_prev = formatar_data(data_str)
    if data_prev is None:
        print(" Data inválida! Use DD/MM/AAAA.")
        return

    responsavel = input("  Responsável     : ").strip()
    if responsavel == "":
        print(" Responsável é obrigatório!")
        return

    novo_id = gerar_id()
    tarefas.append([novo_id, id_animal, tipo, data_prev, responsavel, "Pendente"])
    print(f"\n Tarefa '{tipo}' para '{animal[1]}' criada com ID #{novo_id}!")



def ler_tarefas():
    """Lista todas as tarefas cadastradas."""
    print("  [R] LISTAR TODAS AS TAREFAS")

    if len(tarefas) == 0:
        print("  Nenhuma tarefa cadastrada ainda.")
        return

    for t in tarefas:
        animal      = buscar_animal_por_id(t[1])
        nome_animal = animal[1] if animal is not None else "Desconhecido"
        print(f"\n  ID        : #{t[0]}")
        print(f"  Animal    : {nome_animal}")
        print(f"  Tipo      : {t[2]}")
        print(f"  Data      : {t[3].strftime('%d/%m/%Y')}")
        print(f"  Responsável: {t[4]}")
        print(f"  Status    : {status_tarefa(t)}")


def ler_tarefa_por_id():
    print(" BUSCAR TAREFA POR ID")
    if len(tarefas) == 0:
        print("  Nenhuma tarefa cadastrada.")
        return

    try:
        id_tarefa = int(input("  ID da tarefa: "))
    except ValueError:
        print(" ID inválido!")
        return

    for t in tarefas:
        if t[0] == id_tarefa:
            animal      = buscar_animal_por_id(t[1])
            nome_animal = animal[1] if animal else "Desconhecido"
            print("  DETALHES DA TAREFA")
            print(f"  ID        : #{t[0]}")
            print(f"  Animal    : {nome_animal}")
            print(f"  Tipo      : {t[2]}")
            print(f"  Data      : {t[3].strftime('%d/%m/%Y')}")
            print(f"  Responsável: {t[4]}")
            print(f"  Status    : {status_tarefa(t)}")
            return

    print(" Tarefa não encontrada!")


def ler_tarefas_por_animal():
    """Lista tarefas filtradas por animal."""
    print("  [R] TAREFAS POR ANIMAL")
    if len(animais) == 0:
        print("  Nenhum animal cadastrado.")
        return

    for a in animais:
        print(f"    #{a[0]} – {a[1]}")

    try:
        id_animal = int(input("  ID do animal: "))
    except ValueError:
        print(" ID inválido!")
        return

    animal = buscar_animal_por_id(id_animal)
    if animal is None:
        print(" Animal não encontrado!")
        return
    print(f"  TAREFAS DE: {animal[1].upper()}")

    encontrou = False
    for t in tarefas:
        if t[1] == id_animal:
            encontrou = True
            print(f"  #{t[0]} | {t[2]:<16} | {t[3].strftime('%d/%m/%Y')} | {t[4]:<12} | {status_tarefa(t)}")

    if not encontrou:
        print("  Nenhuma tarefa para este animal.")


def atualizar_tarefa():
    print("ATUALIZAR TAREFA")
    if len(tarefas) == 0:
        print("  Nenhuma tarefa cadastrada.")
        return                                                                                                 
    for t in tarefas:
        animal      = buscar_animal_por_id(t[1])
        nome_animal = animal[1] if animal else "?"
        print(f"  #{t[0]} | {t[2]:<16} | {nome_animal:<12} | {status_tarefa(t)}")

  
    try:
        id_tarefa = int(input("  ID da tarefa a atualizar: "))
    except ValueError:
        print(" ID inválido!")
        return

    tarefa = None
    for t in tarefas:
        if t[0] == id_tarefa:
            tarefa = t
            break

    if tarefa is None:
        print(" Tarefa não encontrada!")
        return

    print(f"  [U] EDITANDO TAREFA #{tarefa[0]}")
    print("  (Pressione ENTER para manter o valor atual)\n")

    print("  Tipos de cuidado:")
    print("  1 – Vacina          2 – Banho")
    print("  3 – Consulta Vet.   4 – Treino")
    print("  5 – Vermifugação    6 – Outro")
    tipos = {
        "1": "Vacina", "2": "Banho", "3": "Consulta Vet.",
        "4": "Treino", "5": "Vermifugação", "6": "Outro"
    }
    opcao_tipo = input(f"\n  Novo tipo (atual: {tarefa[2]}) [1-6]: ").strip()
    if opcao_tipo != "":
        if opcao_tipo not in tipos:
            print(" Opção inválida! Tipo não alterado.")
        else:
            tarefa[2] = tipos[opcao_tipo]

    data_str = input(f"  Nova data (atual: {tarefa[3].strftime('%d/%m/%Y')}) DD/MM/AAAA: ").strip()
    if data_str != "":
        nova_data = formatar_data(data_str)
        if nova_data is None:
            print("  Data inválida! Data não alterada.")
        else:
            tarefa[3] = nova_data

    novo_resp = input(f"  Novo responsável (atual: {tarefa[4]}): ").strip()
    if novo_resp != "":
        tarefa[4] = novo_resp
    print(f"\n  Status atual: {status_tarefa(tarefa)}")
    print("  1 – Pendente   2 – Concluída")
    opcao_status = input("  Novo status (ENTER para manter): ").strip()
    if opcao_status == "1":
        tarefa[5] = "Pendente"
    elif opcao_status == "2":
        tarefa[5] = "Concluída"

    print(f"\n  Tarefa #{tarefa[0]} atualizada com sucesso!")
  



def deletar_tarefa():
    print("DELETAR TAREFA")
    if len(tarefas)==0:
        print("Nenhuma tarefa cadastrada.")
        return

    for t in tarefas:
        animal      = buscar_animal_por_id(t[1])
        nome_animal = animal[1] if animal else "?"
        print(f"  #{t[0]} | {t[2]:<16} | {nome_animal:<12} | {status_tarefa(t)}")

    try:
        id_tarefa = int(input("  ID da tarefa a deletar: "))
    except ValueError:
        print(" ID inválido!")
        return

    for i in range(len(tarefas)):
        if tarefas[i][0] == id_tarefa:
            animal      = buscar_animal_por_id(tarefas[i][1])
            nome_animal = animal[1] if animal else "?"
            tipo        = tarefas[i][2]

            print(f"\nDeseja deletar a tarefa '{tipo}' de '{nome_animal}'?")
            confirmacao = input("  Digite S para confirmar: ").strip().upper()

            if confirmacao == "S":
                tarefas.pop(i)
                print(f"\n Tarefa '{tipo}' deletada com sucesso!")
            else:
                print("\n Operação cancelada.")
            return

    print(" Tarefa não encontrada!")



def resumo_geral():
    print("           RESUMO GERAL")

    total_animais = len(animais)
    total_tarefas = len(tarefas)
    concluidas    = 0
    pendentes     = 0
    atrasadas     = 0
    hoje          = data_hoje()

    for t in tarefas:
        if t[5] == "Concluída":
            concluidas += 1
        elif t[3] < hoje:
            atrasadas  += 1
        else:
            pendentes  += 1

    print(f" Animais cadastrados  : {total_animais}")
    print(f" Total de tarefas     : {total_tarefas}")
    print(f" Concluídas           : {concluidas}")
    print(f" Pendentes            : {pendentes}")
    print(f" Atrasadas            : {atrasadas}")
    print(f"\n Data de hoje         : {hoje.strftime('%d/%m/%Y')}")
    


def menu_leitura():
    while True:
        print("CONSULTAR TAREFAS")
        print("  1 – Listar todas as tarefas")
        print("  2 – Buscar tarefa por ID")
        print("  3 – Listar tarefas por animal")
        print("  0 – Voltar")
        opcao = input("  Opção: ").strip()

        if opcao == "1":
            ler_tarefas()
        elif opcao == "2":
            ler_tarefa_por_id()
        elif opcao == "3":
            ler_tarefas_por_animal()
        elif opcao == "0":
            break
        else:
            print(" Opção inválida!")


def menu_tarefas():
    while True:
        print("     MENU – TAREFAS (CRUD)")
        print("  1 – Criar tarefa")
        print("  2 – Consultar tarefas")
        print("  3 – Atualizar tarefa")
        print("  4 – Deletar tarefa")
        print("  0 – Voltar")

        opcao = input("  Opção: ").strip()

        if opcao == "1":
            criar_tarefa()
        elif opcao == "2":
            menu_leitura()
        elif opcao == "3":
            atualizar_tarefa()
        elif opcao == "4":
            deletar_tarefa()
        elif opcao == "0":
            break
        else:
            print(" Opção inválida!")
    
def sugerir_cuidados():
    print("\n  SUGESTÕES DE CUIDADOS")
    
    if len(animais) == 0:
        print("  NENHUM ANIMAL CADASTRADO.")
        return
    
    print("\n  ANIMAIS DISPONÍVEIS: ")
    for a in animais:
        print(f"    #{a[0]} – {a[1]} ({a[2]})")

    try:
        id_buscado = int(input("\n  ID DO ANIMAL: "))
    except ValueError:
        print("  ID INVÁLIDO!")
        return
    
    animal = buscar_animal_por_id(id_buscado)
    if animal is None:
        print("  ANIMAL NÃO ENCONTRADO!")
        return
    
    nome = animal[1]
    especie = animal[2].lower()
    idade = animal[4]
    
    try:
        idade = int(idade)

    except (ValueError, TypeError):
        idade = 0
        
    print(f"\n  SUGESTÕES PARA {nome.upper()} ({especie}):\n")
        
    if especie == "cão" or especie == "cao":
        print("  • BANHO E TOSA A CADA 30 DIAS.")
        print("  • PASSEIOS DIÁRIOS DE PELO MENOS 30 MINUTOS.")
        print("  • VERMIFUGAÇÃO A CADA 3 MESES.")
        print("  • VACINAS: V10 ANUAL E ANTIRRÁBICA ANUAL.")
        
    elif especie == "gato":
        print("  • CAIXA DE AREIA LIMPA DIARIAMENTE.")
        print("  • ARRANHADORES E BRINQUEDOS.")
        print("  • VACINAS: V4 FELINA ANUAL E ANTIRRÁBICA ANUAL.")
        print("  • VERMIFUGAÇÃO A CADA 3 MESES.")

    else:
        print("  • CONSULTE UM VETERINÁRIO ESPECIALISTA NA ESPÉCIE.")
        print("  • VERIFIQUE NECESSIDADES ESPECÍFICAS DE DIETA E ESPAÇO.")

    if idade <= 1:
        print("\n  • FILHOTE: MANTER VACINAS E FERMIFUGAÇÃO EM DIA.")
        print("  • ALIMENTAÇÃO ESPECÍFICA PARA FILHOTES.")
        print("  • SOCIALIZAÇÃO PRECOCE É FUNDAMENTAL.")
        
    elif idade >= 8:
        print("\n  • SÊNIOR: CHECK-UP VETERINÁRIO A CADA 6 MESES.")
        print("  • ATENÇÃO A ARTICULAÇÕES E PESO. ")
        print("  • DIETA ADAPTADA PARA A IDADE. ")
        
    try:
        saude = int(animal[6])
    except (ValueError, TypeError, IndexError):
        saude = 0
    
    if saude == 2:
        print("\n  ESTADO ESTÁVEL: MONITORAR DE PERTO E AGENDAR CONSULTA!")
    elif saude == 3:
        print("\n ESTADO RUIM: ENCAMINHAR AO VETERINÁRIO COM URGÊNCIA!")

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

def sugerir_adotantes():
   print("\n SUGESTÕES DE ADOTANTES COMPATÍVEIS")
 
   if len(animais) == 0:
       print("NENHUM ANIMAL CADASTRADO.")
       return
 
   print("\nANIMAIS DISPONÍVEIS:")
   for a in animais:
       print(f"    #{a[0]} – {a[1]} ({a[2]})")

   try:
       id_buscado = int(input("\nID DO ANIMAL: "))
   except ValueError:
       print("ID INVÁLIDO")
       return
 
   animal = buscar_animal_por_id(id_buscado)
   if animal is None:
       print("ANIMAL NÃO ENCONTRADO.")
       return
 
   print(f"\n PERFIL DO ADOTANTE IDEAL PARA {animal[1].upper()}")
   print("(RESPONDA AS PERGUNTAS PARA CALCULAR A COMPATIBILIDADE)\n")

   nome = input("NOME DO ADOTANTE: ").strip()
 
   pref = input("PREFERÊNCIA DA ESPÉCIE (cão, gato, outro): ").strip()
 
   quintal_resp = input("TEM QUINTAL OU ÁREA EXTERNA?: ").strip().lower()
   quintal = quintal_resp == "s"
 
   criancas_resp = input("TEM CRIANÇAS EM CASA?: ").strip().lower()
   criancas = criancas_resp == "s"
 
   exp_resp = input("TEM EXPERIÊNCIAS COM PETS?: ").strip().lower()
   experiencia = exp_resp == "s"
 
   adotante = {
       "nome": nome,
       "preferencia_especie": pref,
       "quintal": quintal,
       "criancas": criancas,
       "experiencia": experiencia
   }
   score = calcular_compatibilidade(animal, adotante)
   barra = "█" * (score // 10) + "░" * (10 - score // 10)
 
   print(f"\n COMPATIBILIDADE DE {nome} COM {animal[1]}:")
   print(f"  [{barra}] {score}%")
 
   if score >= 70:
       print("\n  ✓ ÓTIMO. RECOMENDADO PARA ADOÇÃO.")
   elif score >= 40:
       print("\n  ~ MÉDIO. VALE UMA CONVERSA.")
   else:
       print("\n  ✗ BAIXA. CONSIDERE OUTRO ANIMAL.")