def numero(a):
    if int(a) % 2 == 0:
        print("Par")
    else:
        print("Impar")
    print(f"Numero inteiro é: {int(a)}")
    
valor = float(input("Digite o valor: "))
numero(valor)