'''Peça ao usuário para preencher um vetor com 7 números e, depois, informe um número a ser buscado. O
programa deve dizer se ele existe no vetor e em qual posição (índice).'''   
numeros = []
numero_igual = False

for i in range (0,7):
    num = int(input(f"Qual o {i + 1} número ? "))
    numeros.append(num)

numero_buscado = int(input("\nQual o número você quer buscar ? "))

for i in range (0,7):
    if numero_buscado == numeros[i]:
        numero_igual = True
        print(f"\nEsse número existe na posição {i + 1}")
    elif numero_buscado != numeros[i]:
        print("Esse número não existe neste vetor")
        break