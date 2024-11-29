menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0.0
limite = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor para depósito: R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido. Tente novamente.")

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            valor = float(input("Informe o valor para saque: R$ "))
            if valor > 0 and valor <= saldo and valor <= limite:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            elif valor > saldo:
                print("Saldo insuficiente.")
            elif valor > limite:
                print("O valor do saque excede o limite de R$500.00.")
            else:
                print("Valor inválido. Tente novamente.")
        else:
            print("Número máximo de saques diários atingido.")

    elif opcao == "e":
        print("\n=== Extrato ===")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("================")

    elif opcao == "q":
        print("Obrigado por usar nosso sistema bancário!")
        break

    else:
        print("Operação inválida. Por favor, selecione novamente.")
