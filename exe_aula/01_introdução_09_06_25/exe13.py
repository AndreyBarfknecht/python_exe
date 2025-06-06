"""A turma C é composta de 60 alunos, e a turma D de 20 alunos.
Escreva um algoritmo que leia o percentual de alunos reprovados na turma C
o percentual de aprovados na turma D, calcule e escreva:
(a) O número de alunos reprovados na turma C; (b) O número de alunos reprovados na turma D.
(c) A porcentagem de alunos reprovados em relação ao total de alunos das duas turmas. """
turmac = 60
turmad = 20
recC = int(input("Quantos alunos da turma C foram reprovados: "))
apD = int(input("Quantos alunos da turma D foram aprovados: "))
apC = turmac - recC

"""A"""


"""B"""
recD = turmad - apD


"""C"""
totalturmas = turmac + turmad
totalrep = totalturmas - apC - apD
porcentagem = (totalrep/totalturmas) * 100
print("Número de alunos reprovado turma C = ",recC)
print("Número de alunos reprovado turma D = ",recD)

print("A porcentagem de alunos reprovado nas duas salas são de",porcentagem,"%")

