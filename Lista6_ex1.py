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

par = 0
impar = 0
parzin = []
imparzin = []

for i in range(6):
    if numeros[i] % 2 == 0:
        par = par + 1
        parzin.append(numeros[i])
    else:
        impar = impar + 1
        imparzin.append(numeros[i])

print("Quantidade de numeros pares:", par)
print("Os numeros pares:", parzin)
print("Quantidade de numeros impares:", impar)
print("Os numeros impares:", imparzin)