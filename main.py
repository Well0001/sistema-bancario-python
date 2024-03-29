from datetime import datetime

saldo = 0
limite_diario = 500
cotntador_de_saques = 0
LIMITE_DE_SAQUES = 3
extrato = ""

horario = datetime.now()
horario_atual = horario.strftime('%d/%m/%y %H:%M')

menu_inicial = """
BEM VINDO AO BANCO !!!

Digite a opção desejada :

-----------------
1) -> Depósito  |
-----------------
-----------------
2) -> Saque     |
-----------------
-----------------
3) -> Extrato   |
-----------------
-----------------
4) -> Sair      |
-----------------
--> """

while True:

    opcao = input(menu_inicial)

    if opcao == "1":

        try:
            valor = float(input("Digite o valor a ser depositado: "))

            if valor > 0:
                saldo += valor
                extrato += f"{horario_atual}, Deposito R${valor:.2f} \n"
            else:
                print("O valor informado está incorreto! tente novamente")

        except Exception as e:
            print("Por favor digite apenas números")


    elif opcao == "2":

        try:
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > limite_diario

            excedeu_saques = cotntador_de_saques >= LIMITE_DE_SAQUES

            if excedeu_saldo:
                print(f"Operação falhou! Você não tem saldo suficiente, Seu saldo atual é R${saldo:.2f}")

            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")

            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")

            elif valor > 0:
                saldo -= valor
                extrato += f"{horario_atual}, Saque: R$ {valor:.2f}\n"
                cotntador_de_saques += 1

            else:
                print("Operação falhou! O valor informado é inválido.")
        except:
            print("Digite um valor númerico para o saque")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n{horario_atual} Saldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
