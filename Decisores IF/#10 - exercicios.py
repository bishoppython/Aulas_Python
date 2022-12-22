#Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar.
# Dica: utilize o operador módulo (resto da divisão): %

#1º Forma

numero = int(input('Digite um inteiro: '))

if (numero % 2) == 0:
    print("Par")
else:
    print("Ímpar")


#2º Forma

numero = int(input('Digite um inteiro: '))

    if numero%2 :
        print("Ímpar")
    else:
        print("Par")

# 3º Forma

numero = int(input('Digite um inteiro: '))

if not (numero % 3):
    print("É múltiplo de 3")
else:
    print("Não é múltiplo de 3")