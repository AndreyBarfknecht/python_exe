"""Exercício 4: Calculadora de Média
● Solicite 3 notas, calcule a média e diga se o aluno está aprovado (média ≥ 6)."""

print("\nBem vindo ao boletim digital 2k25. (de somente 3 notas)\n")
num1 = float(input("Digite a primeira nota do aluno e pressione (ENTER): "))
num2 = float(input("Digite a segunda nota do aluno e pressione (ENTER): "))
num3 = float(input("Digite a primeira nota do aluno e pressione (ENTER): "))
media = (num1+num2+num3) / 3
print("a media do aluno foi :",round(media,2))
if(media < 6):
    print("Aluno Reprovado")
else:
    print("Aluno Aprovado")