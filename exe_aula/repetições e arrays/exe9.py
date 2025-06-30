'''Solicite 5 números, armazene em um vetor e, ao final, exiba os números na ordem inversa da que foram
digitados.'''


numeros = []


for i in range (0,5): # loop que pega a lista dos numeros
    numeros.append(int(input(f"Qual o {i + 1}° número ? ")))

numeros_invertido = list(reversed(numeros))

print(numeros_invertido)
    



