n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3

print(f"\nMédia final: {media:.2f}")

if media < 3.0:
    print("Conceito: Reprovado")
elif media < 7.0:
    print("Conceito: Exame")
    exame = 14 - media
    print(f"Você precisa tirar no mínimo {exame:.2f} no exame para ser aprovado.")
else:
    print("Conceito: Aprovado")
    
#na minha cabeca pra passar na recuperacao tirar uma nota que somado a media e dividindo por dois e que seja igual a 7 ((nota da rec + media) / 2) = 7