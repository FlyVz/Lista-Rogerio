a = 0
contador = 0
positivo = 0
negativo = 0
quantidadeP = 0
quantidadeN = 0

while contador < 100:
    a = input("Digite um numero inteiro: ")
    if a >= 0: 
        positivo += a
        quantidadeP += 1
    else:
        negativo -= a
        quantidadeN += 1
    
    
    contador += 1
    

print(positivo - negativo)
print(positivo)
print(negativo)   
print(positivo / quantidadeP)     
print(negativo / quantidadeN)     
    