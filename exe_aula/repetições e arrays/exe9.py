'''Solicite 5 números, armazene em um vetor e, ao final, exiba os números na ordem inversa da que foram
digitados.'''


numeros = []
numeros_invertido = []

for i in range (0,5): # loop que pega a lista dos numeros
    num = int(input(f"Qual o {i + 1}° número ? "))
    numeros.append(num)

for i in range (4,-1,-1): # loop que pega a lista e inverte os numeros
    n = numeros[i]
    numeros_invertido.append(n)
    
print(numeros_invertido)

    



