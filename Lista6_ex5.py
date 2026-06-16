a = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
b = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

print("Digite os valores da lista A:")
a[0] = float(input("A: "))
a[1] = float(input("A: "))
a[2] = float(input("A: "))
a[3] = float(input("A: "))
a[4] = float(input("A: "))
a[5] = float(input("A: "))

print("Digite os valores da lista B:")
b[0] = float(input("B: "))
b[1] = float(input("B: "))
b[2] = float(input("B: "))
b[3] = float(input("B: "))
b[4] = float(input("B: "))
b[5] = float(input("B: "))

a[0] = a[0] + b[0]
a[1] = a[1] + b[1]
a[2] = a[2] + b[2]
a[3] = a[3] + b[3]
a[4] = a[4] + b[4]
a[5] = a[5] + b[5]

print("Lista A apos a soma:")
print(a)
