a = float(input("Digite o valor do lado a: "))
b = float(input("Digite o valor do lado b: "))
c = float(input("Digite o valor do lado c: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("forma um triangulo")
    if a == b == c:
        print("Triangulo equilatero")
    elif a == b or a == c or b == c:
        print("Triangulo isosceles")
    else:
        print("Triangulo escaleno")
else:
    print("Nao forma um triangulo")