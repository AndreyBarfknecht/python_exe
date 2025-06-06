"""Um motorista de taxi deseja calcular o rendimento de seu carro na praça.
Sabendo-se que o preço do combustível é de R$ 4,50 , escreva um algoritmo para ler:
a marcação do Hodômetro (Km) no início do dia, a marcação (Km) no final do dia, o número
de litros de combustível gasto e o valor total (R$) recebido dos passageiros. Calcular e
escrever: a média do consumo em Km/L e o lucro (líquido) do dia."""

hodometroinicial = int(input("Hodômetro (km) início:  "))
hodometrofinal = int(input("Hodômetro (km) final:  "))
litroscombustivel = int(input("Quantos litros de combustível foram gastos: "))
dinheirorecebido = float(input("Quantos (R$) foi ganho: "))
precogasolini = 4.50

"""Dizer os KM/L"""
kml = (hodometrofinal - hodometroinicial) / litroscombustivel
print("\nMédia de consumo -->",round(kml,2),"KM/l")

"""E dizer o lucro líquido do dia"""
lucro = dinheirorecebido -  (litroscombustivel * precogasolini) 
print("\nEle lucrou: R$",lucro)