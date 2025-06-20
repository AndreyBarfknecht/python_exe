"""Um mercado está vendendo frutas com a seguinte tabela de preços:
Até 5 Kg
Morango: R$ 5,00 p/Kg
Maçã: R$ 3,00 p/Kg

Acima de 5 Kg
Morango: R$ 4,00 p/Kg
Maçã:R$ 2,00 p/Kg
"""
kgmorango = float(input("Quantos KG de morango foi comprado: "))
kgmaca = float(input("Quantos KG de maça foi comprado: "))
precomorango = 0
precomaca = 0
if kgmorango <= 5:
    precomorango = 5

else:
    precomorango = 4

if kgmaca <= 5:
    precomaca = 3
else:
    precomaca = 2




totalmorango = kgmorango * precomorango
totalmaca = kgmaca * precomaca
print(totalmorango,totalmaca)


