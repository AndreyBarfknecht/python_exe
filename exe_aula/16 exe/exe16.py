"""A equipe McLaren deseja calcular o número mínimo de litros que deverá colocar
 no tanque de seu carro para que ele possa percorrer um determinado número de
  voltas até o primeiro reabastecimento. Escreva um algoritmo que leia o comprimento
   da pista (em metros), o número total de voltas a serem percorridas no grande prêmio,
    o número de reabastecimentos desejados, e o consumo de combustível do carro (em Km/L).
     """

comprimentoDapista = float(input("Qual o comprimento da pista (em Metros): "))
numeroTotalVoltas = float(input("Qual o núemro total de voltas: "))
numeroReabastecimento = float(input("Quantos reabastecimento vai ter no Grande Prêmio: "))
comsumocombustivel = float(input("Qual o consumo da F1 (em Km.l): "))
"""Calcular e escrever o número mínimo de litros necessários para percorrer até o primeiro
      reabastecimento. Obs: Considere que o número de voltas entre os reabastecimentos é o mesmo."""

comprimentoDapistaemKM = comprimentoDapista / 1000 #transformar M em KM
minimoLitrosNecessario = (numeroTotalVoltas / numeroReabastecimento) * comprimentoDapistaemKM / comsumocombustivel
print("\nMínimo de liros necessário para percirrer até o primeiro reabastecimento --> ",round(minimoLitrosNecessario,2),"L")


