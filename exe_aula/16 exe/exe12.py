"""Escreva um algoritmo para ler o número de eleitores de um município,
o número de votos brancos, nulos e válidos. Calcular e escrever o
percentual que cada um representa em relação ao total de eleitores. """

"""input"""

votosbrancos = int(input("Quantos votos em Branco teve: "))
votosnulos = int(input("Quantos votos nulo teve: "))
votosvalido = int(input("Quantos votos validos teve: "))
eleitores = votosbrancos+votosnulos+votosvalido
porcentagembranco =  (votosbrancos / eleitores) * 100
porcentagemnulos =  (votosnulos / eleitores) * 100
porcentagemvalidos =  (votosvalido / eleitores) * 100
print("\ntotal de eleitores: ",eleitores)
print("\n",round(porcentagembranco,2),"% Votos brancos\n",round(porcentagemnulos,2),"% Votos nulos\n",round(porcentagemvalidos,2)," %Votos valido")






"""processing"""


"""output"""
