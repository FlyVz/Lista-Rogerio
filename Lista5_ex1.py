def temp(a):
    f = (a * 1.8) + 32

    print(f"A temperatura em fahrenheit é: {f}")
    
def tamanho(metro):
    cent = metro * 100
    
    print(f"O tamanho em cm é: {cent}cm")

condicao = 1

while condicao != 0:
    print("Digite 1 para converter Celsius para Fahreinheit")
    print("Digite 2 para converter metros para cm")
    print("Digite 3 para sair")
    
    opcao = 0
    
    opcao = int(input("Digite o que deseja acessar: "))
    
    if opcao == 1:
        temperatura = float(input("Digite a temperatura em celsius: "))
        temp(temperatura)
        
    elif opcao == 2:
        comprimento = float(input("Digite o tamanho em metros: "))
        tamanho(comprimento)
    elif opcao == 3:
        break
    else:
        print("Digite uma opcao valida")
    
    
