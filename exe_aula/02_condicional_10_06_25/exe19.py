"""Escreva um algoritmo para ler as coordenadas (X,Y) de um ponto no sistema cartesiano
 e  Escreva o quadrante ao qual o ponto pertence.  Considere que o usuário não informará
 nenhuma coordenada  igual a zero."""


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
else:
    print("Quad A")

