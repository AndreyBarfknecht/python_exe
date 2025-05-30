"""Exercício 5: Contagem Progressiva
● Escreva um programa que conte de 1 a 10 e mostre cada número."""

num = [1,2,3,4,5,6,7,8,9,10]
for n in num:
    print(n)

    # Alternativa usando range()
print("Usando range():")
for numero in range(1, 11):  # range(1, 11) gera números de 1 até 10 (o 11 não é incluído)
    print(numero)

for num in range(1,11):
    print(num)