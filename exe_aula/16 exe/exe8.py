"""Escreva um algoritmo para ler o salário mensal e o percentual de reajuste.
Calcular e escrever o valor do novo salário. """
salariomensal = float(input("Qual o seu salário mensal: "))
percentualreajuste = float(input("Qual o percentual de reajuste(%): "))
total = (salariomensal / 100) * percentualreajuste + salariomensal
print("O salário após o reajuste é de: ",total)

