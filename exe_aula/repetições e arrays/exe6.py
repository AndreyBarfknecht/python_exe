'''Solicite 10 números, armazene em um vetor e calcule a soma de todos os valores.'''
numeros = []
for i in range (0,10):
    num = int(input(f"Qual o {i + 1}° número: "))
    numeros.append(num)
total = sum(numeros)
print(f"Os numeros digitados foram {numeros}")
print(f"A soma de todos o valores é --> { total}")