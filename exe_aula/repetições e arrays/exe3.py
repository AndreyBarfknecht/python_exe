"""A prefeitura de uma cidade fez uma pesquisa entre seus habitantes,
coletando dados sobre o salário e número de filhos. A prefeitura deseja saber:
      a) média do salário da população; 
      b) média do número de filhos; 
      c) maior salário; 
      d) percentual de pessoas com salário até R$100,00. 
O final da leitura de dados se dará com a entrada de um salário negativo. (Use o comando WHILE)  """
# declaração
total_salario = 0
total_filhos = 0
contador_habitantes = 0
maior_salario = 0
percentual_salarios_100 = 0

while True: # condição para repetir o loop até digitar um salario negativo
    salario = int(input(f"\nQual o valor do salário: R$"))
    if salario < 0: # se digitar salario negativo para o codigo
        break
    if salario <= 100: # % de salario ate 100
        percentual_salarios_100 += 1
    filhos = int(input(f"\nQuantos filhos o habitante tem: "))
    total_salario += salario # somar todos os salrio
    total_filhos += filhos # somar os filhos
    if salario > maior_salario: # descobrir o maior salario
        maior_salario = salario
    contador_habitantes += 1 # qntd de habitantes p/ média

media_salario = total_salario / contador_habitantes # media dos salarios
media_filhos = total_filhos / contador_habitantes # media dos filhos
PercentualSalario = (percentual_salarios_100 / contador_habitantes) * 100 # % dos salarios ate 100


print(f"\nA média de sálarios é de R$:{media_salario}")
print(f"\nA média de filhos é de {media_filhos}")
print(f"\nO maior sálario é R$:{maior_salario}")
print(f"\nO percentual de pessoas que  ganham até R$100 é de {PercentualSalario}%")