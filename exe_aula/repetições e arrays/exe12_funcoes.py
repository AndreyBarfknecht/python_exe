'''Um sistema gerador de boletin escolar que recebe 4 notas do alunos e devolve se ele foi aprovado
ou reprovado. utilize funções para cada operação.
extra: Utilizando python, gere um pdf com as notas do aluno e a situação dele.'''
import gerador_pdf_boletim

def soma(lista_notas): # função para somar as notas
    resultado = sum(lista_notas)
    return resultado

def media(soma): # funcao para fazer a media das notas
    resultado = soma / 4
    return resultado

def main(): # funcao principal
    lista_notas = [] # array notas
    nome_aluno = input("\nQual o nome do Aluno: ")
    for i in range (0,4): # loop para pegar as notas 
        notas = float(input(f"Qual a {i + 1}° nota do {nome_aluno} : "))
        lista_notas.append(notas) # guardar as notas no array
    total_notas = soma(lista_notas) # fazer a somas das notas
    media_final = media(total_notas) # fazer a media das notas
    if media_final >= 7: # sitiação do aluno aprovado/recuperacao/reprovado
        situacao = "Aprovado"
    elif media_final > 5 and media_final < 6.99:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    
    print(f"\nNome do aluno:{nome_aluno}\nNotas:{lista_notas}\nMédia:{media_final}\nSituação:{situacao}") # mostrar o resultado de tudo
    gerador_pdf_boletim.criar_boletim_pdf(nome_aluno, lista_notas, media_final, situacao)
main()