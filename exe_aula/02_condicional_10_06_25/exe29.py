"""Escreva um algoritmo que leia as medidas dos lados de um triângulo e escreva Se ele é EQUILÁTERO,
ISÓSCELES ou ESCALENO. OBS: Equilátero: 3 lados iguais; Isósceles: 2 lados iguais; Escaleno: 3 lados diferentes.
"""
import time

print ("\nVamos descobrir que tipo de triângulo é!!!")
l1 = float(input("\nQual a medida do primeiro lado do triângulo : "))
l2 = float(input("\nQual a medida do segundo lado do triângulo: "))
l3 = float(input("\nQual a medida do terceito lado do triângulo: "))
print("----------Calculando-----------")
time.sleep(1)
if l1 == l2 == l3:
    print("O triângulo é EQUILÁTERO (3 lados iguais)")
elif l1 != l2 != l3:
    print("O triângulo é ESCALENO (3 lados diferentes)")
else:
    print("O triângulo é ISÓSCELES (2 lados iguais)")