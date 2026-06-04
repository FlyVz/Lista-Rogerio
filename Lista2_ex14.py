n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3

if media <= 5.0:
    print("Nota final: E")
elif media > 5.0 and media <= 6.0:
    print("Nota final: D")
elif media > 6.0 and media <= 7.0:
    print("Nota final: C")
elif media > 7.0 and media <= 8.0:
    print("Nota final: B")
else:
    print("Nota final: A")