def numero(a):
    if a >= 0: 
        print("Numero positivo")
    else:
        print("Numero negativo")
        
    print(f"Numero inteiro é {int(a)}")
    
valor = float(input("Digite um valor: "))

numero(valor)