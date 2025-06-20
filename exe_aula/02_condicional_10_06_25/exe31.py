"""Escreva um algoritmo que leia o valor de 3 ângulos de um triângulo e
escreva Se o triângulo \né ACUTÂNGULO, RET NGULO ou OBTUS NGULO. OBS: Retângulo: um ângulo reto.
Obtusângulo: um ângulo obtuso; Acutângulo: 3 ângulos agudos.
"""

angulo1 = float(input("\nQual o primeiro ângulo (ex 90°)? "))
angulo2 = float(input("\nQual o segundo ângulo (ex: 90°)? "))
angulo3 = float(input("\nQual o terceiro ângulo (ex: 90°)? "))

if angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
    print("\nÉ um triângulo ACUTÂNGULO")
elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
    print("\nÉ um triângulo RETÂNGULO")
elif angulo1 > 90 < 180 or angulo2 > 90 < 180 or angulo3 > 90 <180:
    print("\nÉ um triângulo OBTUSÂNGULO")

