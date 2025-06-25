"""imports"""
from random import randint
print("Bem vindo ao LUDO ")
print("Regras do jogo: ")
print("-Mínimo de 2 dois jogadores ")
print("-Máximo de 10 jogadores ")
print("Insira 1 para jogar ou outro numero/letra para pular o jogo ")
replay = 0
while replay == 0:

    """funções"""
    separador = ' '
    """listas e variaveis"""
    j = 0
    k = 0
    t = 0
    tem_ganhador = 6
    lista_jog = []
    tabuleiro = []
    posicao_jog = []
    continuar = 0
    num_casas = 40

    num_jog = int(input("Insira o numero de jogadores "))
    if (1 < num_jog <11):

        """---------------------------------------------------------insere o nome dos jogadores -----------------------"""
        for p in range(num_jog):
            lista_jog.append(input("insira o nome do jogador "))
            p += 1
        """---------------------------------------------------------lista os nomes dos jogadores ---------------------"""
        for i in range(len(lista_jog)):
            print(f"Jogador ", i, " é ", lista_jog[i])
            i += 1
            if i > len(lista_jog):
                continue
        """---------------------------------------------------------define a posição dos jogadores para 0--------------"""
        k = 0
        for k in range(num_jog):
            posicao_jog.append(0)
            print(f"posicao de {lista_jog[k]} foi definida como {posicao_jog[k]} ")
            k += 1
            if k > num_jog:
                print("continuou")
                continue
        p = 0
        s = 0
        """---------------------------------------------------------enche a matriz de traços ------------------------"""

        for p in range(num_jog):
            tabuleiro.append([])
            for s in range(num_casas):
                tabuleiro[p].append("-")
        print()
        """VOLTA 4 CASAS"""
        """cria posições de azar"""
        for i in range(2):
            pos = randint(1, 39)
            for j in range(len(lista_jog)):
                tabuleiro[j][pos] = "A"
                ''
        """AVANCA 4 CASAS"""
        """cria posições de sort"""
        for i in range(2):
            pos = randint(1, 39)
            for j in range(len(lista_jog)):
                tabuleiro[j][pos] = "V"
                ''
        """mostra posições de sort/azar"""
        for p in range(num_jog):
            print(f"{lista_jog[p]}")
            for s in range(num_casas):
                print(tabuleiro[p][s], end="")
                ''
            print()


        while tem_ganhador == 6:

            escolha = 0
            t = 0
            for t in range(num_jog):
                posij = 0
                escolha = bool(input(f"jogador {lista_jog[t]} digite 1 para jogar "))
                if escolha == 1:
                    posij = (randint(1, 6))
                    print(f"DADO: {posij}")
                else:
                    print("Você escolheu passar a vez")
                    posij = 0
                    print(f"DADO: {posij}")
                """lista_jog = []
                    tabuleiro = []
                    posicao_jog = []"""
                for i in range(39):
                    posicao_tab = posicao_jog[t]
                    tabuleiro[t][posicao_tab] = "-"
                posicao_jog[t] += posij
                if(posicao_jog[t]<40):
                    if tabuleiro[t][posicao_jog[t]] == 'A':
                        print("Você foi contemplado com o avanço de 4 casas")
                        posicao_jog[t] += 4
                    if tabuleiro[t][posicao_jog[t]] == 'V':
                        print("Você foi contemplado com o atraso de 4 casas")
                        posicao_jog[t] -= 4
                    i = 0

                print(f"Sua nova posicao é {posicao_jog[t]}")
                if posicao_jog[t] >= 40:
                    tem_ganhador = 12
                    break
                """aqui muda tabuleiro"""
                i = 0
                for i in range(39):
                    posicao_tab = posicao_jog[t]
                    tabuleiro[t][posicao_tab] = "x"
                """mostra posicao atual"""
            t = 0
            for t in range(num_jog):
                print(lista_jog[t])
                s = 0
                for s in range(num_casas):
                    print(tabuleiro[t][s], end="")
                print()
        print(f"Parabéns!!! Jogador {lista_jog[t]} é o vencedor")
        replay = int(input("Escolha 0 para replay e 1 para sair"))
    else:
        print("somente é permitido ente 2 e 10 jogadores!")
