"""Exercício 8: Calculadora Simples
● Pergunte ao usuário a operação desejada (+, -, *, /) e dois números, depois realize a operação."""

for x in range(1,999):
    op = input("\nQual a operação matemática você quer fazer (+,-,*,/): ")
    #ADIÇÃO
    if(op == "+"):
        num1 = float(input("\nDigite o primeiro número da soma e pressione (Enter): "))
        num2 = float(input("\nDigite o segundo número e pressione (Enter): "))
        print("\nO resultado da adição",num1 ,"+", num2,"=", (num1+num2))
    #SUBTRAÇÃO
    if(op == "-"):
        num1 = float(input("\nDigite o primeiro número da subtração e pressione (Enter): "))
        num2 = float(input("\nDigite o segundo número e pressione (Enter): "))
        print("\nO resultado da subtração",num1 ,"-", num2,"=", (num1-num2))
    #MULTIPLICAÇÃO
    if(op == "*"):
        num1 = float(input("\nDigite o primeiro número da multiplicação e pressione (Enter): "))
        num2 = float(input("\nDigite o segundo número e pressione (Enter): "))
        print("\nO resultado da multiplicação",num1 ,"*", num2,"=", (num1*num2))
    #DIVISÃO
    if(op == "/"):
        num1 = float(input("\nDigite o primeiro número da divisão e pressione (Enter): "))
        num2 = float(input("\nDigite o segundo número e pressione (Enter): "))
        print("\nO resultado da divisão",num1 ,"/", num2,"=", (num1/num2))

    x = input("\nSe quiser sair digite (sair) se não pressione enter: ")
    if(x == "sair"):
        break

