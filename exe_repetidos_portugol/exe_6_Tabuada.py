"""Exercício 6: Tabuada
● Solicite um número e imprima a tabuada de 1 a 10 desse número."""
num = int (input("Digite o número que você quer saber a tabuada: "))
for x in range(1,11):
    print(num," X ",x," = ",num*x,"\n")
