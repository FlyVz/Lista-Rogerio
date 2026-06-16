A = []

n1 = int(input("Digite um numero: "))
A.append(n1)
n2 = int(input("Digite um numero: "))
A.append(n2)
n3 = int(input("Digite um numero: "))
A.append(n3)
n4 = int(input("Digite um numero: "))
A.append(n4)
n5 = int(input("Digite um numero: "))
A.append(n5)
n6 = int(input("Digite um numero: "))
A.append(n6)
n7 = int(input("Digite um numero: "))
A.append(n7)
n8 = int(input("Digite um numero: "))
A.append(n8)

maior = A[0]

for i in range(8):
    if A[i] > maior:
        maior = A[i]
print("O maior valor da lista e:", maior)