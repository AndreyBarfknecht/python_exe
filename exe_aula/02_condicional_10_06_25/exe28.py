"""Um posto está vendendo combustíveis com a seguinte tabela de descontos:
--------------------------------------------------------------------------------
Combustível             Litros               Desconto
Álcool                 Até 20                 3%
                      Mais de 20               5%
Gasolina               Até 15                   3,5% 
                     Mais de 15                6%
--------------------------------------------------------------------------------
Escreva um algoritmo que leia o número de litros vendidos,
 o tipo de combustível (codificado da seguinte forma: 1-álcool 2-Gasolina),
 calcule e imprima o valor a ser pago pelo cliente, sabendo-se que o preço da gasolina
 é de R$ 1,90 o litro e o álcool R$ 1,28.
"""
import time
from decimal import Decimal

precoalcool = Decimal("1.28")
precogasolina = Decimal("1.90")
desconto_alcool3 = Decimal("0.03")
desconto_alcool5 = Decimal("0.05")
desconto_gasolina3_5 = Decimal("0.035")
desconto_gasolina6 = Decimal("0.06")


preco_por_litro = Decimal("0")
percentual_desconto = Decimal('0')

tipocombustivel = input("\nQual o o tipo de combustível (1-álcool 2-Gasolina): ")

if tipocombustivel == "1": #se o combustivel for alcool
    time.sleep(1)
    print("\n----------Combustível selecionado ALCOOL----------")
    litrosvendidos = Decimal(input("\nQuantos litros foram vendidos: "))
    preco_por_litro = precoalcool
    if litrosvendidos <= 20: #% do desconto
        percentual_desconto = desconto_alcool3        
    elif litrosvendidos > 20:
        percentual_desconto = desconto_alcool5

elif tipocombustivel == "2": #se for gasolina
    time.sleep(1)
    print("\n----------Combustível selecionado GASOLINA----------")
    litrosvendidos = Decimal(input("\nQuantos litros foram vendidos: "))
    preco_por_litro = precogasolina
    if litrosvendidos <= 15: # % do desconto
      percentual_desconto = desconto_gasolina3_5
    elif litrosvendidos > 15:
        percentual_desconto = desconto_gasolina6
else:
    print("\nOpção de combustível invalida")
    
#calculo
valor_bruto = litrosvendidos * preco_por_litro
valor_desconto = valor_bruto * percentual_desconto
valor_a_pargar = valor_bruto - valor_desconto

valor_total_formatado = round(valor_a_pargar,2)

print("\nCalculando o valor da compra")
time.sleep(2)
print("\nResumo da Compra")
print(f"Litros vendidos = {litrosvendidos} L")
print(f"Preço por litro: R$ {preco_por_litro}")
print(f"Valor bruto: R${round(valor_bruto,2)}")
print(f"Desconto ({round(percentual_desconto*100,2)}%) = R${round(valor_desconto,2)} ")
print("---------------------------------")
print(f"Valor total a pagar: R$ {valor_total_formatado}")
