tamanho = int(input("Quantos elementos terá o array? "))

meu_array = []

for i in range(tamanho):
    valor = int(input(f"Digite o valor da posição {i}: "))
    meu_array.append(valor)

print("Array preenchido:")
print(meu_array)
