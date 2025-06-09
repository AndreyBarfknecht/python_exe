"""Um determinado bar cobra 10% de gorjeta sobre o valor total consumido de cada mesa.
 Leia o valor total consumido de uma mesa e informe o total a pagar."""
valormesa = float(input("Qual o valor da conta ?"))
taxa = 0.10

print("\nValor da gorjeta = ",round(valormesa*taxa,2))
print("\nO total a pargar é: ",(valormesa*taxa)+valormesa)

 