"""Escreva um algoritmo para ler as notas da 1ª e 2ª avaliações de um aluno,
 calcular a média e Escreva Se este aluno foi APROVADO, REPROVADO ou Se está EM EXAME.
 Escreva também a média calculada. OBS: Para ter direito ao exame o aluno deve obter média mínima 5.5.
"""

nota1 = float(input("Qual a primeira nota do aluno: "))
nota2 = float(input("Qual a segunda nota do aluno: "))
media = (nota1+nota2) / 2
if media < 5.5:
    print("Aluno está Reprovado, média =",media)
elif media >= 7:
    print("Aluno está aprovado, média =",media)
else:
    print("Aluno está em Exame, média = ",media)
