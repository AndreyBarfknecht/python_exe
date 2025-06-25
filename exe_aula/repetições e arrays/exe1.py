"""Escrever um algoritmo que lê 5 valores para a,
um de cada vez, e conta quantos destes valores são negativos, escrevendo esta informação. """

tamanho = 5 
negativo = 0
a = []

for i in range (tamanho):
    valor = int(input(f"Digite o número {i}: "))
    a.append(valor)
    if valor < 0:
        negativo += 1
print(f"Nesse array tem {negativo} números negativos")