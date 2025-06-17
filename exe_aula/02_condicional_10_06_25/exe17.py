"""Escreva um algoritmo para ler 3 valores e escreva a soma dos 2 maiores.
 Considere que o usuário não informará valores iguais."""

a = int(input("\nQual o primeiro valor: "))
b = int(input("\nQual o segundo valor: "))
c = int(input("\nQual o terceiro valor: "))

if a > b and a > c:
    print("\n",a,"É o maior")
    nummaior1 = a
    if b > c:
        nummaior2 = b
    else:
        nummaior2 = c
    print("\nA soma dos dois números maiores é",nummaior1,"+",nummaior2,"=",(nummaior1+nummaior2))

elif b > a and b > c:
    print("\n",b,"É o maior")
    nummaior1 = b
    if a > c:
        nummaior2 = a
    else:
        nummaior2 = c
    print("\nA soma dos dois números maiores é",nummaior1,"+",nummaior2,"=",(nummaior1+nummaior2))

elif c > a and c > b:
    print("\n",c,"É o maior")
    nummaior1 = c
    if a > b:
        nummaior2 = a
    else:
        nummaior2 = b
    print("\nA soma dos dois números maiores é",nummaior1,"+",nummaior2,"=",(nummaior1+nummaior2))

else:
    print("\nos valores são iguais")