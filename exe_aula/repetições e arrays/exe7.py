'''Solicite 6 números, armazene em um vetor, e informe qual é o maior e qual é o menor número digitado.'''

numeros = []

for i in range (0,6):
    num = int(input(f"Qual o {i + 1}° número ? "))
    numeros.append(num)

maior_numero = max(numeros)
menor_numero = min(numeros)

print(f"Esse é o maior numero do vetor --> {maior_numero}")
print(f"Esse é o menor numero do vetor --> {menor_numero}")