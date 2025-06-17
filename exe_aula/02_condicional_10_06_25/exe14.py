"""Acrescente as seguintes mensagens à solução do exercício anterior conforme o caso.
Caso o número de lados seja inferior a 3 Escreva: NÃO E’ UM POLÍGONO.
Caso o número de lados seja superior a 5 Escreva: POLÍGONO NÃO IDENTIFICADO.
OBS: Considere que o usuário poderá informar qualquer valor para o número de lados."""

numlados = int(input("\nQuantos lados tem o seu polígono ? "))

if numlados < 3:
    print("\nNão é um póligono")

elif numlados == 3:
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

else :
    print("\nPóligono não identificado")