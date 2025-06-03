"""Uma revendedora de carros usados paga a seus funcionários vendedores um 
salário fixo por mês, = 3000
mais uma comissão fixa por cada carro vendido. = 2
 Além disso, ela também adiciona ao salário de
cada vendedor 5% do valor das vendas por ele efetuadas.
 Escrever um algoritmo que lê o número
do vendedor, o salário fixo, o número de carros por ele vendidos, o valor total de suas vendas
e a comissão fixo que recebe por carro vendido e, sem seguida, calcule o salário do vendedor
juntamente com o seu número de identificação."""
numeroidentifucação = input("Qual o número de identificação do funcionario: ")
qtdcarrosvendidos = int(input("Quantos carros foram vendidos: "))
valorcarrovendido = float(input("Qual o valor de carros vendidos: "))

salariofixo = 3000
comisaofixa = 2.5

valorvendas = ((valorcarrovendido / 100) * comisaofixa * qtdcarrosvendidos + valorcarrovendido * qtdcarrosvendidos )
valortotal = ((valorvendas /100)*5 + valorvendas +salariofixo)
print("\nnumero de identificação do funcionario:",numeroidentifucação,"\n","e o salário dele é: ",valortotal)









