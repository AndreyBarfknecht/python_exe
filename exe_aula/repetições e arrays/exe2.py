"""Escrever um algoritmo que lê um valor N inteiro e positivo e que imprime a tabuada de N para valores de 1 a 10."""
num = int(input("Qual número você quer saber a tabuada: "))

for i in range (11):
    print(f"{num} X {i} = {num * i} ")
    

