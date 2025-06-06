# -*- coding: utf-8 -*-

# PASSO 1: Criar nossa "biblioteca" ou "dicionário" de letras gigantes.
# Cada letra é uma chave, e seu valor é uma lista de strings (as "fatias").
# É MUITO IMPORTANTE que todas as listas tenham o mesmo número de strings (mesma altura).
# Neste caso, todas as letras têm 5 linhas de altura.
LETRAS_GIGANTES = {
    'A': [
        "  A  ",
        " A A ",
        "AAAAA",
        "A   A",
        "A   A"
    ],
    'B': [
        "BBBB ",
        "B   B",
        "BBBB ",
        "B   B",
        "BBBB "
    ],
    'C': [
        " CCC ",
        "C   C",
        "C    ",
        "C   C",
        " CCC "
    ],
    'D': [
        "DDDD ",
        "D   D",
        "D   D",
        "D   D",
        "DDDD "
    ],
    'E': [
        "EEEEE",
        "E    ",
        "EEE  ",
        "E    ",
        "EEEEE"
    ],
    'F': [
        "FFFFF",
        "F    ",
        "FFF  ",
        "F    ",
        "F    "
    ],
    'G': [
        " GGG ",
        "G    ",
        "G GGG",
        "G   G",
        " GGG "
    ],
    'H': [
        "H   H",
        "H   H",
        "HHHHH",
        "H   H",
        "H   H"
    ],
    'I': [
        "IIIII",
        "  I  ",
        "  I  ",
        "  I  ",
        "IIIII"
    ],
    'J': [
        "JJJJJ",
        "    J",
        "    J",
        "J   J",
        " JJJ "
    ],
    'K': [
        "K   K",
        "K  K ",
        "KK   ",
        "K  K ",
        "K   K"
    ],
    'L': [
        "L    ",
        "L    ",
        "L    ",
        "L    ",
        "LLLLL"
    ],
    'M': [
        "M   M",
        "MM MM",
        "M M M",
        "M   M",
        "M   M"
    ],
    'N': [
        "N   N",
        "NN  N",
        "N N N",
        "N  NN",
        "N   N"
    ],
    'O': [
        " OOO ",
        "O   O",
        "O   O",
        "O   O",
        " OOO "
    ],
    'P': [
        "PPPP ",
        "P   P",
        "PPPP ",
        "P    ",
        "P    "
    ],
    'Q': [
        " QQQ ",
        "Q   Q",
        "Q Q Q",
        "Q  QQ",
        " QQQQ"
    ],
    'R': [
        "RRRR ",
        "R   R",
        "RRRR ",
        "R  R ",
        "R   R"
    ],
    'S': [
        " SSS ",
        "S    ",
        " SSS ",
        "    S",
        " SSS "
    ],
    'T': [
        "TTTTT",
        "  T  ",
        "  T  ",
        "  T  ",
        "  T  "
    ],
    'U': [
        "U   U",
        "U   U",
        "U   U",
        "U   U",
        " UUU "
    ],
    'V': [
        "V   V",
        "V   V",
        "V   V",
        " V V ",
        "  V  "
    ],
    'W': [
        "W   W",
        "W   W",
        "W M W",
        "WWMWW",
        "W   W"
    ],
    'X': [
        "X   X",
        " X X ",
        "  X  ",
        " X X ",
        "X   X"
    ],
    'Y': [
        "Y   Y",
        " Y Y ",
        "  Y  ",
        "  Y  ",
        "  Y  "
    ],
    'Z': [
        "ZZZZZ",
        "   Z ",
        "  Z  ",
        " Z   ",
        "ZZZZZ"
    ],
    ' ': [ # Caractere de espaço, para separar palavras
        "     ",
        "     ",
        "     ",
        "     ",
        "     "
    ]
}

def imprimir_em_letras_gigantes(texto):
    """
    Função principal que organiza e imprime o texto em letras gigantes.
    """
    # Define a altura das letras (pegando o tamanho da lista de qualquer letra)
    altura_das_letras = len(LETRAS_GIGANTES['A'])
    
    # Converte o texto para maiúsculas para corresponder às chaves do dicionário
    texto = texto.upper()
    
    # PASSO 3: Loop principal, que passa por cada "andar" ou "linha" das letras
    for i in range(altura_das_letras):
        linha_para_imprimir = ""
        
        # Loop interno, que passa por cada caractere do texto do usuário
        for caractere in texto:
            # Verifica se o caractere existe na nossa biblioteca, senão usa espaço
            if caractere in LETRAS_GIGANTES:
                # Pega a fatia correta (a linha 'i') do caractere atual
                fatia_da_letra = LETRAS_GIGANTES[caractere][i]
                linha_para_imprimir += fatia_da_letra + "  " # Adiciona a fatia e um espaço
            else:
                # Se não encontrar a letra, adiciona um espaço em branco no lugar
                fatia_de_espaco = LETRAS_GIGANTES[' '][i]
                linha_para_imprimir += fatia_de_espaco + "  "

        # Após montar a linha completa com as fatias de todas as letras, imprime
        print(linha_para_imprimir)


# --- Execução do Programa ---
if __name__ == "__main__":
    # PASSO 2: Pedir a entrada do usuário
    nome = input("Digite seu nome ou uma palavra: ")
    print("\nPreparando para imprimir...\n")
    imprimir_em_letras_gigantes(nome)
    print("\nPronto!\n")