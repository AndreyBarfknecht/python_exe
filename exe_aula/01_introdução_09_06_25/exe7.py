"""Dados 3 valores positivos (a, b, c), calcular: (a) área do triângulo retângulo com base a e altura b;
(b) área do retângulo com base a e altura c; (c) área do trapézio com base maior a, base menor b e altura c."""




"""Área  do triangulo retangulo"""
a = int(input("Vamos calcular a área do triangulo retangulo\nQual a hipotenusa --> "))
b = int(input("Qual o cateto1 --> "))
c = int(input("Qual o cateto2 --> "))
areatriangulo = (b*c) / 2
print("A área do triangulo é ",areatriangulo)
"""Área do retangulo """
a = int(input("\nAgora vamos calcular a área do retangulo\nQual a base do retangulo --> "))
b = int(input("Qual a altura --> "))
arearetangulo = a * b
print ("A área do retangulo é ",arearetangulo)
"""Área do trapézio"""
a = int(input("Vamos calcular a área do trapézio\nQual a base maior --> "))
b = int(input("Qual a base menor --> "))
c = int(input("Qual a altura --> "))
areatrapezio = ((a+b)*c) /2
print("A área do trapézio é ",areatrapezio)
"""Outputs"""





