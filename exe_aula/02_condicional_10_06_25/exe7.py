"""Escreva um algoritmo para ler 2 valores (considere que não serão lidos
valores iguais) e escrevê-los em ordem crescente."""
print("\nEscreva dois números e o PC vai organizar em ordem crescente\n ")
num1 = input("Escreva o primeiro número: ")
num2 = input("Escreva o segundo número: ")
if num1 > num2:
 print ("Ordem crescente = ",num2,num1)
elif num2 > num1:
 print("Ordem crescente = ",num1,",",num2)
