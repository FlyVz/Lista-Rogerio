soma = 0
quantidade = 0
continuar = 's'
maior = 0
menor = 0
while continuar == 's':
    numero = float(input("Digite um número: "))
    soma = soma + numero
    quantidade = quantidade + 1
    if quantidade == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero 
    continuar = input("Deseja digitar outro número? (s/n): ")

media = soma / quantidade
print("A média dos números é:", media)
print("O maior número digitado foi:", maior)
print("O menor número digitado foi:", menor)
