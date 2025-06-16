"""Tendo como entrada a altura e o sexo
(codificado da seguinte forma:
 1 : feminino
 2 : masculino) de uma pessoa,
construa um algoritmo que calcule e imprima seu peso ideal, utilizando as seguintes fórmulas:
para homens: 		(72.7 * h) - 58
para mulheres:  	(62.1 * h) - 44.7
"""
genero = input("Qual o seu gênero (M ou F)? ")
altura = float(input("Qual a sua altura (em metros ex: 1.84)? "))
if genero == "M":
    imc = (72.7 * altura) - 58
elif genero == "F":
    imc = (62.1 * altura) - 44.7

print("Seu peso ideau é = ",round(imc,2))



