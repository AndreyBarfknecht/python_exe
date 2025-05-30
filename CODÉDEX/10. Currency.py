
print("Bem vindo ao cambiador digital.")
Colombianpesos = float(input("Quantos pesos Colombianos você tem ?"))
Peruviansoles = float(input("Quantos soles Peruanos você tem ?"))
Brazilianreais = float(input("Quantos reis Brasileiros você tem ?"))

"""cotacaoColombia = Colombianpesos / 4161,5
cotacaoPeruana = Peruviansoles / 3,62
cotacaoBrazil = Brazilianreais / 5,71
dolar = cotacaoColombia+cotacaoPeruana+cotacaoBrazil"""
total = Colombianpesos* 0.00024 + Peruviansoles * 0.28 + Brazilianreais * 0.18


print ("Você tem $: ",total)