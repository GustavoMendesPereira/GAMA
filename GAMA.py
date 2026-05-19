def cadastro_do_estudante():

  print("Cadastro do estudante")

  estudante = {

    "Nome": str(input("Digite o nome do estudante: ")),

    "Matricula" : int(input("Digite a matricula do estudante: ")),

    "Idade" : int(input("Digite a idade do estudante: ")),

    "Serie" : str(input("Digite a serie do estudante: ")),

    "Contato do responsavel": int(input("Digite o número do responsavel: ")),

    "Sexo:" : str(input("Qual sexo do estudante? ")),

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





def materia_fisolofia():

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





estudante_cadastrado = cadastro_do_estudante()

print("\nDados do Estudante")

for chave, valor in estudante_cadastrado.items():

  print(f"{chave}: {valor}")





historia = materia_historia()

print(historia)





geografia = materia_geografia()

print(geografia)





fisica = materia_fisica()

print(fisica)





educacao_fisica = materia_educacao_fisica()

print(educacao_fisica)





matematica = materia_matematica()

print(matematica)





portugues = materia_portugues()

print(portugues)





quimica = materia_quimica()

print(quimica)





biologia = materia_biologia()

print(biologia)





filosofia = materia_fisolofia()

print(filosofia)





sociologia = materia_sociologia()

print(sociologia)
