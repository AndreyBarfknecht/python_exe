'''Escreva um algorítmo que leia 5 arrays, cada um contendo as notas de 5  alunos, 
e calcule a média de cada array que é a média final.'''

print("Bem vindo a calculadora de médias")


total_n1 = 0
total_n2 = 0
total_n3 = 0
total_n4 = 0
total_n5 = 0

# Primeiro array, guardando 5 notas 
print("\nMatéria 1")
for a in range (5):
    nota = float(input(f"Qual a {a+1}° nota --> "))
    total_n1 += nota

print("\nMatéria 2")
for a in range (5):
    nota = float(input(f"Qual a {a+1}° nota --> "))
    total_n2 += nota

print("\nMatéria 3")
for a in range (5):
    nota = float(input(f"Qual a {a+1}° nota --> "))
    total_n3 += nota
print("\nMatéria 4")
for a in range (5):
    nota = float(input(f"Qual a {a+1}° nota --> "))
    total_n4 += nota
print("\nMatéria 5")
for a in range (5):
    nota = float(input(f"Qual a {a+1}° nota --> "))
    total_n5 += nota

print("\nMédia final 1 =",(total_n1) / 5)
print("\nMédia final 2 =",(total_n2) / 5)
print("\nMédia final 2 =",(total_n3) / 5)
print("\nMédia final 2 =",(total_n4) / 5)
print("\nMédia final 2 =",(total_n5) / 5)