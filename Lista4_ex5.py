n = int(input("Digite um numero: "))
a = 0

for i in range(1, n):
    if n % i == 0:
        a = a + i
        
if a == n:
    print(1)  
else:
    print(0)  