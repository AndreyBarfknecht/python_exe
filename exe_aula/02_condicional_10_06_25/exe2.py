"""Acrescente ao exercício acima a mensagem
‘Você foi REPROVADO! Estude mais.’ caso a média calculada seja menor que 8,0.
"""
nota1 = float(input("\nQual a primeira nota (ex:8.5): "))
nota2 = float(input("\nQual a segunda nota (ex:8.5): "))
media = (nota1+nota2) / 2
print("\nA sua média foi: ",round(media,2))
if media >= 8:
    print("\nPARABÉNS! Você foi aprovado.")
else:
    print("\nVocê foi REPROVADO! Estude mais.")