"""Exercício 7: Maior de Três Números
● Solicite três números e exiba qual é o maior."""
print("Está com dificuldade de saber qual número é maior? digite aqui.\n")
num1 = float(input("Digite o primeiro número: \n"))
num2 = float(input("Digite o segundo número: \n"))
num3 = float(input("Digite o terceiro número: \n"))

if (num1 > num2):
    if(num1>num3):
        print(round(num1,2),"É o maior")
    elif(num3 > num2):
        print(round(num3,2),"É o maior")
    else:
        print(round(num2,2),"É o maior")
elif(num2 > num3):
    print(round(num2,2),"É o maior")
else:
    print(round(num3,2),"É o maior")