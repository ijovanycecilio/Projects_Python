#Desafio: Criando um sistema bancário

""" Objetivo Geral
    Criar um sistema bancário com as operações: sacar, depositar
    e visualizar extrato.  """

print("Seja bem vindo ao Banco ABC")

menu = """
=====|Digite a opção desejada:|===

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "d":

        deposito = float(input("Qual o valor deseja depositar:"))

        if deposito > 0:
            saldo = saldo + deposito
            extrato = extrato + " \nDepósito: R$ {:.2f}".format(deposito)
            

    if opcao == "s":

        if numero_saques >= LIMITE_SAQUES:
            print("Número de Saques diários excedido, favor tentar novamente amanhã")

        else:
            saque = float(input("Qual o valor deseja sacar:"))

            numero_saques = numero_saques + 1

            if saque <= limite:
                if saque <= saldo:
                    saldo = saldo - saque
                    extrato= extrato + " \nSaque: R$ {:.2f}".format(saque)

                else:
                    print("Não possui saldo suficiente, seu saldo atual é de {:.2f}".format(saldo))
            
            else:
                print("Limite de saques excedido, favor tentar um valor menor R$ {}".format(limite))

    if opcao == "e":
        print("=="*5,"extrato","=="*5)
        print(extrato)
        print("\nO saldo atual é: R$ {:.2f}".format(saldo))
        print("=="*12)

    if opcao == "q":
        print("Obrigado, volte sempre!")
        break
    
    elif opcao != "d" and opcao != "s" and opcao != "e" and opcao != "q":
        print("Operação inválida,por favor selecione novamente a operação desejada")
        

