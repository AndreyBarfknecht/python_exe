"""Escreva um algoritmo para ler as notas das duas avaliações de um aluno no semestre,
calcular e Escreva a média semestral e a seguinte mensagem: ‘PARABÉNS! Você foi aprovado’
 somente Se o aluno foi aprovado (considere 8.0 a nota mínima para aprovação)."""

nota1 = float(input("\nQual a primeira nota (ex:8.5): "))
nota2 = float(input("\nQual a segunda nota (ex:8.5): "))
media = (nota1+nota2) / 2
print("\nA sua média foi: ",round(media,2))
if media >= 8:
    print("\nPARABÉNS! Você foi aprovado.")
else:
    print("")



