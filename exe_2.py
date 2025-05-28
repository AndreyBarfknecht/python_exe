nome = input("Qual o seu nome? ")
idade = int (input("Qual a sua idade? "))
nota1 = float(input("Qual a primeira nota? "))
nota2 = float(input("Qual a segunda nota? "))
nota3 = float(input("Qual a terceira nota? "))
soma = nota1+nota2+nota3
media = soma / 3

print ("\nO nome do aluno é",nome,"\na idade é",idade,"\na média do aluno é:", round(media,2) )

if(media < 5):
    print ("O aluno está reprovado")
elif(media >= 7):
    print ("O aluno está aprovado")
else:
    print("O aluno está de recuperação")

    

