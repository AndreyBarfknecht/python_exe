'''Escreva um algorítmo que leia 5 arrays, cada um contendo as notas de 5  alunos, 
e calcule a média de cada array que é a média final.'''

print("Bem vindo a calculadora de médias")

notas1 = []
notas2 = []
notas3 = []
notas4 = []
notas5 = []

# Primeiro array, guardando 5 notas 
print("\nMatéria 1")
for a in range (5):
    nota = float(input(f"Qual a {a+1}° nota --> "))
    notas1.append(nota)

print("\nMatéria 2")
for a in range (5):
    nota = float(input(f"Qual a {a+1}° nota --> "))
    notas2.append(nota)

print("\nMatéria 3")
for a in range (5):
    nota = float(input(f"Qual a {a+1}° nota --> "))
    notas3.append(nota)

print("\nMatéria 4")
for a in range (5):
    nota = float(input(f"Qual a {a+1}° nota --> "))
    notas4.append(nota)

print("\nMatéria 5")
for a in range (5):
    nota = float(input(f"Qual a {a+1}° nota --> "))
    notas5.append(nota)


print("\nMédia final 1 =",(notas1[0]+notas1[1]+notas1[2]+notas1[3]+notas1[4]) / 5)
print("\nMédia final 2 =",(notas2[0]+notas2[1]+notas2[2]+notas2[3]+notas2[4]) / 5)
print("\nMédia final 2 =",(notas3[0]+notas3[1]+notas3[2]+notas3[3]+notas3[4]) / 5)
print("\nMédia final 2 =",(notas4[0]+notas4[1]+notas4[2]+notas4[3]+notas4[4]) / 5)
print("\nMédia final 2 =",(notas5[0]+notas5[1]+notas5[2]+notas5[3]+notas5[4]) / 5)