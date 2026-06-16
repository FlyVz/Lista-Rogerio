numeros = []

n1 = int(input("Digite um numero: "))
numeros.append(n1)
n2 = int(input("Digite um numero: "))
numeros.append(n2)
n3 = int(input("Digite um numero: "))
numeros.append(n3)
n4 = int(input("Digite um numero: "))
numeros.append(n4)
n5 = int(input("Digite um numero: "))
numeros.append(n5)
n6 = int(input("Digite um numero: "))
numeros.append(n6)
n7 = int(input("Digite um numero: "))
numeros.append(n7)
n8 = int(input("Digite um numero: "))
numeros.append(n8)
mult2 = []
mult3 = []

for i in range(8):
    if numeros[i] % 2 == 0:
        mult2.append(numeros[i])
for i in range(8):
    if numeros[i] % 3 == 0:
        mult3.append(numeros[i])

print("Numeros multiplos de 2:", mult2)
print("Numeros multiplos de 3:", mult3)