"""Escreva um algoritmo para ler as dimensões de uma cozinha retangular
 (comprimento, largura e altura), calcular e escrever a quantidade de
  caixas de azulejos para se colocar em todas as suas paredes
  (considere que não será descontado a área ocupada por portas e janelas).
  Cada caixa de azulejos possui 2m2. """
"""multiplicar a largura de cada parede pela altura do ambiente,"""

comprimento = float(input("Qual o comprimento da cozinha: "))
largura = float(input("Qual a largura da cozinha: "))
altura = float(input("Qual a altura da cozinha: "))

m2cozinha = largura * comprimento
print(m2cozinha)