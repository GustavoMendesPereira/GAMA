def cadastro_do_estudante():
    print("\nCadastro do estudante")
    estudante = {
        "Nome": str(input("Digite o nome do estudante: ")),
        "Matricula": int(input("Digite a matricula do estudante: ")),
        "Idade": int(input("Digite a idade do estudante: ")),
        "Serie": str(input("Digite a serie do estudante: ")),
        "Contato do responsavel": int(input("Digite o número do responsavel: ")),
        "Sexo": str(input("Qual sexo do estudante? ")),
    }
    return estudante


def materia_historia():
    print("\n--- Notas: História ---")
    n_trabalho = float(input("Digite a nota de trabalho: "))
    n_prova = float(input("Digite a nota da prova: "))
    n_tarefa = float(input("Digite a nota de tarefa: "))
    faltas = int(input("Total de faltas (Limite 50): "))

    if n_trabalho >= 11 or n_prova >= 11 or n_tarefa >= 11:
        print("Nota inválida! Digite uma nota entre 0 e 10.")
        n_trabalho = float(input("Digite a nota de trabalho: "))
        n_prova = float(input("Digite a nota da prova: "))
        n_tarefa = float(input("Digite a nota de tarefa: "))

    media = (n_trabalho + n_prova + n_tarefa) / 3
    porcentagem_faltas = (faltas / 200) * 100

    if media >= 6 and faltas <= 50:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    return {
        "Média Final": f"{media:.2f}",
        "Total de Faltas": faltas,
        "Frequência": f"{100 - porcentagem_faltas}%",
        "Resultado": situacao
    }


def materia_geografia():
    print("\n--- Notas: Geografia ---")
    n_trabalho = float(input("Digite a nota de trabalho: "))
    n_prova = float(input("Digite a nota da prova: "))
    n_tarefa = float(input("Digite a nota de tarefa: "))
    faltas = int(input("Total de faltas (Limite 50): "))

    if n_trabalho >= 11 or n_prova >= 11 or n_tarefa >= 11:
        print("Nota inválida! Digite uma nota entre 0 e 10.")
        n_trabalho = float(input("Digite a nota de trabalho: "))
        n_prova = float(input("Digite a nota da prova: "))
        n_tarefa = float(input("Digite a nota de tarefa: "))

    media = (n_trabalho + n_prova + n_tarefa) / 3
    porcentagem_faltas = (faltas / 200) * 100

    if media >= 6 and faltas <= 50:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    return {
        "Média Final": f"{media:.2f}",
        "Total de Faltas": faltas,
        "Frequência": f"{100 - porcentagem_faltas}%",
        "Resultado": situacao
    }


def materia_fisica():
    print("\n--- Notas: Física ---")
    n_trabalho = float(input("Digite a nota de trabalho: "))
    n_prova = float(input("Digite a nota da prova: "))
    n_tarefa = float(input("Digite a nota de tarefa: "))
    faltas = int(input("Total de faltas (Limite 50): "))

    if n_trabalho >= 11 or n_prova >= 11 or n_tarefa >= 11:
        print("Nota inválida! Digite uma nota entre 0 e 10.")
        n_trabalho = float(input("Digite a nota de trabalho: "))
        n_prova = float(input("Digite a nota da prova: "))
        n_tarefa = float(input("Digite a nota de tarefa: "))

    media = (n_trabalho + n_prova + n_tarefa) / 3
    porcentagem_faltas = (faltas / 200) * 100

    if media >= 6 and faltas <= 50:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    return {
        "Média Final": f"{media:.2f}",
        "Total de Faltas": faltas,
        "Frequência": f"{100 - porcentagem_faltas}%",
        "Resultado": situacao
    }


def materia_educacao_fisica():
    print("\n--- Notas: Educação Física ---")
    n_trabalho = float(input("Digite a nota de trabalho: "))
    n_prova = float(input("Digite a nota da prova: "))
    n_tarefa = float(input("Digite a nota de tarefa: "))
    faltas = int(input("Total de faltas (Limite 50): "))

    if n_trabalho >= 11 or n_prova >= 11 or n_tarefa >= 11:
        print("Nota inválida! Digite uma nota entre 0 e 10.")
        n_trabalho = float(input("Digite a nota de trabalho: "))
        n_prova = float(input("Digite a nota da prova: "))
        n_tarefa = float(input("Digite a nota de tarefa: "))

    media = (n_trabalho + n_prova + n_tarefa) / 3
    porcentagem_faltas = (faltas / 200) * 100

    if media >= 6 and faltas <= 50:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    return {
        "Média Final": f"{media:.2f}",
        "Total de Faltas": faltas,
        "Frequência": f"{100 - porcentagem_faltas}%",
        "Resultado": situacao
    }


def materia_matematica():
    print("\n--- Notas: Matemática ---")
    n_trabalho = float(input("Digite a nota de trabalho: "))
    n_prova = float(input("Digite a nota da prova: "))
    n_tarefa = float(input("Digite a nota de tarefa: "))
    faltas = int(input("Total de faltas (Limite 50): "))

    if n_trabalho >= 11 or n_prova >= 11 or n_tarefa >= 11:
        print("Nota inválida! Digite uma nota entre 0 e 10.")
        n_trabalho = float(input("Digite a nota de trabalho: "))
        n_prova = float(input("Digite a nota da prova: "))
        n_tarefa = float(input("Digite a nota de tarefa: "))

    media = (n_trabalho + n_prova + n_tarefa) / 3
    porcentagem_faltas = (faltas / 200) * 100

    if media >= 6 and faltas <= 50:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    return {
        "Média Final": f"{media:.2f}",
        "Total de Faltas": faltas,
        "Frequência": f"{100 - porcentagem_faltas}%",
        "Resultado": situacao
    }


def materia_portugues():
    print("\n--- Notas: Português ---")
    n_trabalho = float(input("Digite a nota de trabalho: "))
    n_prova = float(input("Digite a nota da prova: "))
    n_tarefa = float(input("Digite a nota de tarefa: "))
    faltas = int(input("Total de faltas (Limite 50): "))

    if n_trabalho >= 11 or n_prova >= 11 or n_tarefa >= 11:
        print("Nota inválida! Digite uma nota entre 0 e 10.")
        n_trabalho = float(input("Digite a nota de trabalho: "))
        n_prova = float(input("Digite a nota da prova: "))
        n_tarefa = float(input("Digite a nota de tarefa: "))

    media = (n_trabalho + n_prova + n_tarefa) / 3
    porcentagem_faltas = (faltas / 200) * 100

    if media >= 6 and faltas <= 50:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    return {
        "Média Final": f"{media:.2f}",
        "Total de Faltas": faltas,
        "Frequência": f"{100 - porcentagem_faltas}%",
        "Resultado": situacao
    }


def materia_quimica():
    print("\n--- Notas: Química ---")
    n_trabalho = float(input("Digite a nota de trabalho: "))
    n_prova = float(input("Digite a nota da prova: "))
    n_tarefa = float(input("Digite a nota de tarefa: "))
    faltas = int(input("Total de faltas (Limite 50): "))

    if n_trabalho >= 11 or n_prova >= 11 or n_tarefa >= 11:
        print("Nota inválida! Digite uma nota entre 0 e 10.")
        n_trabalho = float(input("Digite a nota de trabalho: "))
        n_prova = float(input("Digite a nota da prova: "))
        n_tarefa = float(input("Digite a nota de tarefa: "))

    media = (n_trabalho + n_prova + n_tarefa) / 3
    porcentagem_faltas = (faltas / 200) * 100

    if media >= 6 and faltas <= 50:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    return {
        "Média Final": f"{media:.2f}",
        "Total de Faltas": faltas,
        "Frequência": f"{100 - porcentagem_faltas}%",
        "Resultado": situacao
    }


def materia_biologia():
    print("\n--- Notas: Biologia ---")
    n_trabalho = float(input("Digite a nota de trabalho: "))
    n_prova = float(input("Digite a nota da prova: "))
    n_tarefa = float(input("Digite a nota de tarefa: "))
    faltas = int(input("Total de faltas (Limite 50): "))

    if n_trabalho >= 11 or n_prova >= 11 or n_tarefa >= 11:
        print("Nota inválida! Digite uma nota entre 0 e 10.")
        n_trabalho = float(input("Digite a nota de trabalho: "))
        n_prova = float(input("Digite a nota da prova: "))
        n_tarefa = float(input("Digite a nota de tarefa: "))

    media = (n_trabalho + n_prova + n_tarefa) / 3
    porcentagem_faltas = (faltas / 200) * 100

    if media >= 6 and faltas <= 50:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    return {
        "Média Final": f"{media:.2f}",
        "Total de Faltas": faltas,
        "Frequência": f"{100 - porcentagem_faltas}%",
        "Resultado": situacao
    }


def materia_filosofia():
    print("\n--- Notas: Filosofia ---")
    n_trabalho = float(input("Digite a nota de trabalho: "))
    n_prova = float(input("Digite a nota da prova: "))
    n_tarefa = float(input("Digite a nota de tarefa: "))
    faltas = int(input("Total de faltas (Limite 50): "))

    if n_trabalho >= 11 or n_prova >= 11 or n_tarefa >= 11:
        print("Nota inválida! Digite uma nota entre 0 e 10.")
        n_trabalho = float(input("Digite a nota de trabalho: "))
        n_prova = float(input("Digite a nota da prova: "))
        n_tarefa = float(input("Digite a nota de tarefa: "))

    media = (n_trabalho + n_prova + n_tarefa) / 3
    porcentagem_faltas = (faltas / 200) * 100

    if media >= 6 and faltas <= 50:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    return {
        "Média Final": f"{media:.2f}",
        "Total de Faltas": faltas,
        "Frequência": f"{100 - porcentagem_faltas}%",
        "Resultado": situacao
    }


def materia_sociologia():
    print("\n--- Notas: Sociologia ---")
    n_trabalho = float(input("Digite a nota de trabalho: "))
    n_prova = float(input("Digite a nota da prova: "))
    n_tarefa = float(input("Digite a nota de tarefa: "))
    faltas = int(input("Total de faltas (Limite 50): "))

    if n_trabalho >= 11 or n_prova >= 11 or n_tarefa >= 11:
        print("Nota inválida! Digite uma nota entre 0 e 10.")
        n_trabalho = float(input("Digite a nota de trabalho: "))
        n_prova = float(input("Digite a nota da prova: "))
        n_tarefa = float(input("Digite a nota de tarefa: "))

    media = (n_trabalho + n_prova + n_tarefa) / 3
    porcentagem_faltas = (faltas / 200) * 100

    if media >= 6 and faltas <= 50:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    return {
        "Média Final": f"{media:.2f}",
        "Total de Faltas": faltas,
        "Frequência": f"{100 - porcentagem_faltas}%",
        "Resultado": situacao
    }



lista_estudantes = []

while True:
    print("\n--- Menu ---")
    print("1. Cadastrar estudante")
    print("2. Ver estudantes cadastrados")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        aluno = cadastro_do_estudante()
        
        aluno["Disciplinas"] = {
            "História": materia_historia(),
            "Geografia": materia_geografia(),
            "Física": materia_fisica(),
            "Educação Física": materia_educacao_fisica(),
            "Matemática": materia_matematica(),
            "Português": materia_portugues(),
            "Química": materia_quimica(),
            "Biologia": materia_biologia(),
            "Filosofia": materia_filosofia(),
            "Sociologia": materia_sociologia()
        }
        
        
        lista_estudantes.append(aluno)
        print(f"\Estudante {aluno['Nome']} cadastrado com sucesso!")

    elif opcao == "2":
        if len(lista_estudantes) == 0:
            print("\nNenhum estudante cadastrado no sistema ainda.")
        else:
            busca = input("\nDigite o Nome ou a Matrícula do aluno para buscar: ")
            aluno_encontrado = False
            
            for aluno in lista_estudantes:
                if busca == aluno["Nome"] or busca == str(aluno["Matricula"]):
                    aluno_encontrado = True
                    
                    print("\n==============================")
                    print("      DADOS DO ESTUDANTE      ")
                    print("==============================")
                    print(f"Nome: {aluno['Nome']}")
                    print(f"Matrícula: {aluno['Matricula']}")
                    print(f"Idade: {aluno['Idade']}")
                    print(f"Série: {aluno['Serie']}")
                    print(f"Contato: {aluno['Contato do responsavel']}")
                    print(f"Sexo: {aluno['Sexo']}")
                    
                    print("\n--- BOLETIM ESCOLAR ---")
                    for materia, notas in aluno["Disciplinas"].items():
                        print(f"\n> {materia}")
                        print(f"  Média: {notas['Média Final']} | Faltas: {notas['Total de Faltas']} | Freq: {notas['Frequência']} | {notas['Resultado']}")
                    print("==============================")
            
            if not aluno_encontrado:
                print("\nEstudante não encontrado no sistema.")

    elif opcao == "3":
        print("\nSaindo do sistema...")
        break

    else:
        print("\nOpção inválida! Tente novamente.")
