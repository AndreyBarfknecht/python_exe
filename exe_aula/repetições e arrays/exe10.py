'''Peça 4 notas, calcule a média e armazene uma mensagem no vetor de saída dizendo se o aluno foi
“Aprovado” ou “Reprovado” (média ≥ 6).'''

quantidade_notas = 4
soma_notas = 0

for i in range (quantidade_notas):
    nota = float(input(f"Qual a {i+1}° nota ? "))
    soma_notas += nota
    
media = soma_notas / quantidade_notas
if media >= 6:
    print(f"Aluno APROVADO com a média = {media}")
else:
    print(f"Aluno REPROVADO com a média = {media}")



# print (soma_notas)