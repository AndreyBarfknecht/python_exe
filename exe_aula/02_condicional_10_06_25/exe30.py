"""Escreva um algoritmo que leia a idade de 2 homens e 2 mulheres
(considere que a idade dos homens será sempre diferente, assim como das mulheres).
 Calcule e escreva a soma das idades do homem mais velho com a mulher mais nova, e
  o produto das idades do homem mais novo com a mulher mais velha."""
homem1 = int(input("\nQual a idade do primeiro homem: "))
mulher1 = int(input("Qual a idade da primeira mulher: "))
homem2 = int(input("\nQual a idade do segundo homem: "))
mulher2 = int(input("Qual a idade da segunda mulher: "))

if homem1 > homem2 and mulher1 > mulher2:
    homemvelho = homem1
    homemnovo = homem2
    mulhervelha = mulher1
    mulhernova = mulher2
else:
    homemvelho = homem2
    homemnovo = homem1
    mulhervelha = mulher2
    mulhernova = mulher1

calculo1 = homemvelho + mulhernova
calculo2 = homemnovo * mulhervelha
print(f"homem mais velho com a mulher mais nova: {homemvelho}+{mulhernova}={calculo1}\nHomem mais novo com a mulher mais velha: {homemnovo}*{mulhervelha}={calculo2}")




