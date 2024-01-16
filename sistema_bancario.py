menu ='''
        (d) Depositar
        (s) Sacar
        (e) Extrato
        (q) Sair
    
'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
saque_total = 0
depositos = []
saques = []

while True:
    opcao = input(menu)
    
    if opcao == "d":
        print("Deposito")
        valor_deposito = float(input("Insira o valor do deposito: "))

        if (valor_deposito) <= 0:
            print("Operação falhou! Por favor, insira um valor valido.")
        else:
            saldo += valor_deposito
            depositos.append(valor_deposito)

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            print("Saque")
            valor_saque = float(input("Insira o valor do saque: "))

            if (valor_saque) > 500:
                print("O valor limite para cada saque é de 500 reais. Por favor, tente novamente com um valor menor.")

            elif (valor_saque) > (saldo+limite):
                print("Não será possivel completar a operação devido a falta de saldo. Por favor, tente novamente com um valor menor.")

            elif valor_saque < 0:
                print("Operação falhou! Por favor, insira um valor valido.")

            else:
                saque_total += valor_saque
                numero_saques += 1
                saldo -= valor_saque
                saques.append(valor_saque)

        else:
            print("Limite de saques atinguido")

    elif opcao == "e":
        print("Extrato")
        print(f'''
            Saldo: {saldo}
            Somatória de saques: {saque_total}
            Depositos: {depositos}
            Saques: {saques}
            ''')
         
    elif opcao == "q":
        break
        
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

