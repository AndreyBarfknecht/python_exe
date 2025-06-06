"""Escreva um algoritmo para ler 2 valores (considere que não serão informados
valores iguais) e escreva o maior deles."""

num1 = float(input("Qual o primeiro número: "))
num2 = float(input("Qual o segundo número: "))

if num1 > num2:
    print(num1)
elif num2 > num1:
    print(num2)
