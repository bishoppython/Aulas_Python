"""Escreva um programa em Python que receba um número correspondente
ao cargo de um funcionário de uma escola e seu salário atual e mostre o
valor do novo salário, com aumento, conforme tabela abaixo:
1 funcionário 45%,
2 funcionário 35%,
3 funcionário 25%,
4 funcionário 15%,
5 funcionário
recebe nenhum aumento."""

while True:
    print("1 - Diretor(a) \n"
          "2 - Conselhero(a) \n"
          "3 - Professor(a) \n"
          "4 - Secretario(a) \n"
          "5 - Zelador(a) \n"
          "0 - sair")
    cargo = int(input("digite o numero de funcionários do cargo especifico: "))
    if cargo == 0:
        print("Obrigador por utilizar o programa!")
        break
    salario = float(input("Digite seu salário: "))
    if cargo == 1:
        profissao = "Diretor"
        reajuste = (salario * 45)/100
        novo_sal = salario + reajuste
        print("Um funcionario do Cargo", profissao, "que ganhava R${:.2f},"
                                                    "houve um aumento de R$ {:.2f}, e passou a receber R$ {:.2f}"
              .format(salario,reajuste,novo_sal))
    if cargo == 2:
        profissao = "Conselheiro"
        reajuste = (salario * 35)/100
        novo_sal = salario + reajuste
        print("Um funcionario do Cargo", profissao, "que ganhava R${:.2f}, houve um aumento de R$ {:.2f}, e passou a receber R$ {:.2f}".format(salario,reajuste,novo_sal))
    if cargo == 3:
        profissao = "Professor"
        reajuste = (salario * 25)/100
        novo_sal = salario + reajuste
        print("Um funcionario do Cargo", profissao, "que ganhava R${:.2f}, houve um aumento de R$ {:.2f}, e passou a receber R$ {:.2f}".format(salario,reajuste,novo_sal))
    if cargo == 4:
        profissao = "Secretaria"
        reajuste = (salario * 15)/100
        novo_sal = salario + reajuste
        print("Um funcionario do Cargo", profissao, "que ganhava R${:.2f}, houve um aumento de R$ {:.2f}, e passou a receber R$ {:.2f}".format(salario,reajuste,novo_sal))
    if cargo == 5:
        profissao = "Zelador"
        #reajuste = (salario * 45/100)
        #novo_sal = salario + reajuste
        print("Um funcionario do Cargo", profissao, "que ganhava R${:.2f} e como não houve alteração a receber R$ {:.2f}".format(salario))


