opcao = ""
sair = ""
saque = 0
deposito = 0
saldo = 0

def depositar(valor):
    if valor <= 0:
        print("Digite um valor valido!")
    elif valor > 0:
        deposito = valor
    
def sacar(valor):
    if valor <= 0:
        print("Digite um valor valido!")
    else:
        saque = valor

while opcao != "sair":
    print("Opcoes disponiveis:")
    print("Saldo")
    print("Deposito")
    print("Saque")
    print("Sair")
    
    opcao = input("Digite o que voce quer acessar: ").lower()
    
    if opcao == "sair":
        break
    
    elif opcao == "saldo":
        print(saldo)
        
    elif opcao == "deposito":
        deposito = float(input("Digite o valor a ser depositado: "))
        depositar(deposito)
        saldo += deposito
        print(saldo)
        
    elif opcao == "saque":
        saque = float(input("Digite o valor a ser sacado: "))
        sacar(saque)
        saldo -= saque
        print(saldo)
    else:
        print("Digite uma opcao valida! ")