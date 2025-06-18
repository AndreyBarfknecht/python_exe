"""Escreva um algoritmo para ler as 4 notas obtidas por um aluno em 4 avaliações. Calcular a média usando
 a seguinte fórmula:
Média = (N1 + (N2 * 2) + (N3 * 3) + N4) / 7
	A seguir imprima o conceito do aluno baseado na seguinte tabela:
Média
Conceito
9,0 ou acima de 9,0 =                A
entre 7,5 (inclusive) e 9,0 =     B
entre 6,0 (inclusive) e 7,5 =     C
abaixo de 6,0 =                   D

"""
n1 = float(input("Qual a primeira nota: "))
n2 = float(input("Qual a segunda nota: "))
n3 = float(input("Qual a terceira nota: "))
n4 = float(input("Qual a quarta nota: "))
media = (n1 + (n2 * 2) + (n3 * 3)+ n4) / 7

print("\nMédia =",round(media,2))
if media >= 9:
    print("conceito A")
elif media >= 7.5 and media < 9:
    print("Conceito B")
elif media >= 6 and media < 7.5:
    print("Conceito C")
elif media < 6:
    print("Conceito D")



