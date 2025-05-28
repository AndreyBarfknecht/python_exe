"""Exercício 3: Número Par ou Ímpar
● Peça um número ao usuário e informe se ele é par ou ímpar."""
num = int(input("\nDigite um número para saber se ele é impar ou par.\n"))

if(num % 2 == 0):
    print("\nEsse número é par")
else:
    print("\nEsse número é impar")
    