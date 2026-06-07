a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if a == 0:
    print("Nao e uma equacao do segundo grau")
else:
    delta = b**2 - 4*a*c

    if delta < 0:
        print("Nao existem raizes reais")
    elif delta == 0:
        r = -b / (2*a)
        print(f"Raiz unica: {r}")
    else:
        r1 = (-b + delta**0.5) / (2*a)
        r2 = (-b - delta**0.5) / (2*a)
        print(f"Raizes : {r1} e {r2}")