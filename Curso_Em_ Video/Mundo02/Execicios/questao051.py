numero = int(input("Digite um numero: "))
cont = 0

for i in range(1, numero + 1, 1):
    if numero % i == 0:
        cont += 1
        print(cont)
        if cont > 2:
            print("numero n e primo")
            break

if cont == 2:
    print("Numero e primo")
