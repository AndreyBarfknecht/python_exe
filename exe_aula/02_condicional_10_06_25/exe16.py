"""Escreva um algoritmo para ler 3 valores e escreva o maior deles.
 Considere que o usuário não informará valores iguais."""
a = int(input("Qual o primeiro valor: "))
b = int(input("Qual o segundo valor: "))
c = int(input("Qual o terceiro valor: "))

if a > b and a > c:
    print(a,"É o maior")
elif b > a and b > c:
    print(b,"É o maior")
elif c > a and c > b:
    print(c,"É o maior")
else:
    print("os valores são iguais")



