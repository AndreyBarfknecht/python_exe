"""Escreva um algoritmo para ler o ano de nascimento de uma pessoa e Escreva uma mensagem
que diga Se ela poderá ou não votar este ano (não é necessário considerar o mês em que ela nasceu).
"""
print("\nVamos saver se você vai votar ou não esse ano!!!")
anonascimento = int(input("\nQual o ano que você nasceu? --> "))
anoatual = 2025
idade = anoatual - anonascimento
idademinima = 16
if idade < idademinima:
    print("\nVocê ainda nao pode votar idade mínima 16 anos\n\nvocê tem:",idade,"anos")
else:
    print("\nVocê já tem o direito de votar\n\nVocê tem:",idade,"anos")