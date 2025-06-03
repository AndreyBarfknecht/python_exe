"""Escreva um algoritmo para ler uma temperatura em graus Fahrenheit,
calcular e escrever o valor correspondente em graus Celsius: C = ((F – 32)*5)/9"""
Fahrenheit = float(input("Qual a temperatura em Fahrenheit: "))
Celcius = ((Fahrenheit - 32)*5/9)
print("Celcius = ",Celcius)