print("Digite 1 se quiser bilhetes unicos")
print("Digite 2 se quiser pacotes com 2 bilhetes")
print("Digite 3 se quiser pacotes com 10 bilhetes \n")

key = int(input("Qual você deseja: "))
valor = float(input("Valor que será investido: "))
quantidade = 0
troco = 0

if key == 1:
    if valor % 1.3 != 0:
        quantidade = int(valor / 1.3)
        troco = valor - (quantidade * 1.3)
        print("Quantidade: ", quantidade)
        print("Troco: ", round(troco, 2))
    else:
        quantidade = valor / 1.3
        print("Quantidade de bilhestes comprados: ", int(quantidade))  
   
elif key == 2:
    if valor % 2.6 != 0:
        quantidade = int(valor / 2.6)
        troco = valor - (quantidade * 2.6)
        print("Quantidade: ", quantidade)
        print("Troco: ", round(troco, 2))
    else:
        quantidade = valor / 2.6
        print("Quantidade de pacotes com 2 bilhetes comprados: ", int(quantidade))  
    
else:
    if valor % 12 != 0:
        quantidade = int(valor / 12)
        troco = valor - (quantidade * 12)
        print("Quantidade: ", quantidade)
        print("Troco: ", round(troco, 2))
    else:
        quantidade = valor / 12
        print("Quantidade de pacotes com 10 bilhetes comprados: ", int(quantidade)) 