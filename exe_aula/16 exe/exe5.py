"""Considere que o aumento dos funcionários de uma empresa é de 8% do salário atual
mais um percentual de produtividade discutido com a empresa. Escrever um algoritmo que
lê o número do funcionário, seu salário atual e o índice de produtividade discutido com a empresa.
Então, escreve o número do funcionário, seu aumento e o valor de seu novo salário. """
funcionariomiguel = 541
salariomiguelatual = (2000.00 / 100) * 8 + 2000.00
indicepruditividade = float(input("qual a porcentagem discutida com a empresa"))
novosalario = (salariomiguelatual / 100) * indicepruditividade + salariomiguelatual

print("Número do funcionario",funcionariomiguel,"\n","indice de produtividade:",indicepruditividade,"\n","O novo salario é de: ",novosalario)


