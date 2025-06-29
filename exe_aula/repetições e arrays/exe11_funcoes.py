'''crie uma calculadora que executa calculos simples como soma, subtração, multiplicação e divisão.
A calculadora deve receber dois números e uma operação, e retornar o resultado do cálculo.
nota: utlize funções para cada operação e uma função principal que chama as outras funções.'''

def soma (numero1,numero2):
    resultado = numero1 + numero2
    return resultado
def subtracao (numero1,numero2):
    resultado = numero1 - numero2
    return resultado
def multiplicacao (numero1,numero2):
    resultado = numero1 * numero2
    return resultado
def divisao (numero1,numero2):
    if numero2 == 0:
        return "Erro: Não é possível dividir por zero."
    else:
        resultado = numero1 / numero2
    return resultado


while True:
    def main():
        numero1 = float(input("Qual o primeiro número: "))
        operacao = input("Qual operação você quer fazer (+,-,*,/) : ")
        numero2 = float(input("Qual o segundo número: "))
        if operacao == "+":
            resultado_operacao = soma(numero1,numero2)
        elif operacao == "-":
            resultado_operacao = subtracao(numero1,numero2)
        elif operacao == "*":
            resultado_operacao = multiplicacao(numero1,numero2)
        elif operacao == "/":
            resultado_operacao = divisao(numero1,numero2)
        else:
            resultado_operacao = "Operação inválida. Por favor, use +, -, * ou /."
        
            

        print(f"{numero1} {operacao} {numero2} = {resultado_operacao}")

    main()

