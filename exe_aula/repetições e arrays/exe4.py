"""Chico tem 1,50 metro e cresce 4 centímetros por ano, enquanto Zé tem 1,30 metro e
cresce 6 centímetros por ano. Construa um algoritmo que calcule e imprima quantos
anos serão necessários para que Zé seja maior que Chico.
"""
chico = 1.50
chico_cresce = 0.04
ze = 1.30
ze_cresce = 0.06
anos = 0

while ze < chico :
    chico += chico_cresce
    ze += ze_cresce
    anos += 1
    

print (f"Zé precisou de {anos} anos para ficar mais alto que Chico")





