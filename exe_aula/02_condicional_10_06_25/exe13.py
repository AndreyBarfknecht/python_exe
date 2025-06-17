"""Escreva um algoritmo para ler o número de lados de um polígono regular, e a medida do lado.
 Calcular e imprimir o seguinte:
Se o número de lados for igual a 3, Escreva: TRI NGULO e o valor do seu perímetro;
Se o número de lados for igual a 4 Escreva: QUADRADO e o valor da sua área;
Se o número de lados for igual a 5 Escreva: PENTÁGONO."""

numlados = int(input("Quantos lados tem o seu polígono ? "))

if numlados == 3:
    print("\nO seu póligo é um Triângulo")
    l1 = int(input("Qual o valor do lado 1: "))
    l2 = int(input("Qual o valor do lado 2: "))
    l3 = int(input("Qual o valor do lado 3: "))
    perimetro = int
    perimetro = l1+l2+l3
    print(perimetro)
elif numlados == 4:
    print("\nO seu póligo é um Quadrado")
    l1 = int(input("Qual o valor do lado: "))
    area = l1 ** l1
    print(area,"²")
elif numlados == 5:
    print("\nO seu póligono é um PENTÁGONO")