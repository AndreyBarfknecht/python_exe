"""Escreva um algoritmo para ler o número de gols marcados
 pelo Grêmio e o número de gols marcados pelo Inter em um GRENAL.
 Escreva o Nome do Vencedor. Caso não haja vencedor deverá ser impresso a palavra EMPATE."""
inter = int(input("\nQuantos gols o INTERNACIONAL fez : "))
gremio = int(input("\nQuantos gols o GREMIO fez : "))
if inter > gremio:
    print("\nINTERNACIONAL foi o vencedor\nINTERNACIONAL",inter,"X GRÊMIO",gremio)
elif gremio > inter:
    print("\nGRÊMIO foi o vencedor\nINTERNACIONAL",inter,"X GRÊMIO",gremio)
else:
    print("\nEMPATE\nINTERNACIONAL",inter,"X GRÊMIO",gremio)

