"""Escreva um algoritmo para ler 3 valores e escrevê-los em ordem crescente.
 Considere que o usuário não informará valores iguais."""
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
numeros = [a,b,c]
numeros_ordenados = sorted(numeros)
print("Os números em ordem crescente são :",numeros_ordenados)

"""if a < b and a < c: # se o 1 numero for o menor  #FORMA USANDO A LÓGICA 
    if b < c:
        print(a,b,c) # se o 2 for menor que o 3
    else:
        print(a,c,b) # se o 3 for menor que o 2

elif b < a and b < c: # se o 2 for o menor
    if a < c:
        print(b,a,c) # se o 1 for menor que o 3
    else:
        print(b,c,a) # se o 3 for menor que o 1


elif c < a and c < b: # se o 3 for o menor 
    if a < b:
        print(c,a,b) # se o 1 for o menor que o 2
    else:
        print(c,b,a) # se o 2 for menor que o 1

else:
    print ("Os números são iguais")"""


