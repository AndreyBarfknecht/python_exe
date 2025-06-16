nome = input("Qual o seu nome? ")
idade = int (input("Qual a sua idade? "))
saldoBancario = float(input("Qual o seu saldo bancário? "))

print("\nhello world, meu nome é %s,\nminha idade é %d\n" %(nome,idade),"\n")

if(idade > 18):
    print("Você é maior de idade\n")
else:
    print("Você é menor de idade\n")

if(saldoBancario > 10000):
    print("Você não é pobre\n")
else:
    print("Você é pobre\n")
