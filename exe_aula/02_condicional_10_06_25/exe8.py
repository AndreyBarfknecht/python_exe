"""Escreva um algoritmo que verifique a validade de uma senha fornecida pelo usuário.
 A senha válida é o número 1234. Deve ser impresso as seguintes mensagens:
ACESSO PERMITIDO caso a senha seja válida
ACESSO NEGADO caso a senha seja inválida."""

senha = input("Qual é a senha: (4 DÍGITOS) ")
if senha == "1234":
    print("ACESSO PERMITIDO")
else:
    print("ACESSO NEGADO")