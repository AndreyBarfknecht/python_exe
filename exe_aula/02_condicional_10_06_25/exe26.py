"""Escreva um algoritmo para ler as coordenadas (X,Y) de um ponto no sistema cartesiano e
Escreva o quadrante ao qual o ponto pertence. Caso o ponto não pertença a nenhum quadrante,
escreva se ele está sobre o eixo X, eixo Y ou na origem. Considere que o usuário poderá informar
qualquer valor para as coordenadas.
"""


# B quad (  x,y   )
# A quad ( -x,y   )
# C quad ( -x,-y  )
# D quad (  x,-y  )

x = int(input("Qual a coordenada X = "))
y = int(input("Qual a coordenada Y = "))

if x > 0 and y > 0:
    print("Quad B")
elif x < 0 and y < 0:
    print("Quad C")
elif x > 0 and y < 0:
    print("Quad D")
elif x < 0 and y > 0:
    print("Quad A")
elif x > 0 and y == 0 :
    print("Ele está localizado sobre o eixo X positivo")
elif x < 0 and y == 0:
    print("Ele está localizado sobre o eixo X negativo")
elif y > 0 and x ==0:
    print("Ele está localizado sobre o eixo y positivo.")
elif y < 0 and x == 0:
    print("Ele está localizado sobre o eixo y negativo.")
else:
    print("Está na origem 0,0")

