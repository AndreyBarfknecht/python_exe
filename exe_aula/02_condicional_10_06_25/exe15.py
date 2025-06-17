"""Escreva um algoritmo para ler 2 valores e uma das seguintes operações a
serem executadas (codificada da seguinte forma: 1.Adição, 2.Subtração, 3.Divisão,
 4.Multiplicação). Calcular e Escreva o resultado dessa operação sobre os dois valores lidos.
"""
num = float(input("Qual operação matemática você quer fazer (1 = Adição,2 = Subtração,3 = Divisão,4 = Multiplicação): ")) 
if num == 1:
    print("\n-------------ADIÇÃO-------------")
    num1 = float(input("\nQual o primeiro valor: "))
    num2 = float(input("\nQual o segundo valor: "))
    total = num1+num2
    print("\nO total DE",num1,"+",num2,"=",total)
elif num == 2:
    print("\n-------------SUBTRAÇÃO-------------")
    num1 = float(input("\nQual o primeiro valor: "))
    num2 = float(input("\nQual o segundo valor: "))
    total = num1-num2
    print("\nO total DE",num1,"-",num2,"=",total)
elif num == 3:
    print("\n-------------DIVISÃO-------------")
    num1 = float(input("\nQual o primeiro valor: "))
    num2 = float(input("\nQual o segundo valor: "))
    total = num1/num2
    print("\nO total DE",num1,"/",num2,"=",total)
elif num == 4:
    print("\n-------------MULTIPLICAÇÃO-------------")
    num1 = float(input("\nQual o primeiro valor: "))
    num2 = float(input("\nQual o segundo valor: "))
    total = num1*num2
    print("\nO total DE",num1,"*",num2,"=",total)

