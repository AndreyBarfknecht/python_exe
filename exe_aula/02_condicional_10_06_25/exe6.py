"""As maçãs custam R$ 0,30 ser forem compradas menos do que uma dúzia,
 e R$ 0,25 ser forem compradas pelo menos doze.  Escreva um algoritmo que
 leia o número de maçãs compradas, calcule e escreva o valor total da compra.
"""

precomaca = int
qtdmacas = int(input("Quantas maças você quer comprar ?(menos de uma dúzia elas custam R$0.30 cada e mais de uma dúzia R$0.25) --> "))
if qtdmacas < 12:
    precomaca = 0.30
elif qtdmacas >= 12:
    precomaca = 0.25

qtdmacas = qtdmacas * precomaca
print("R$ ",round(qtdmacas,2))