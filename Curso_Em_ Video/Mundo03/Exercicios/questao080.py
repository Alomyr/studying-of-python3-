numeros = []
pares = []
impares = []
start = True
count = 0


def escolha(opt):
    match opt:
        case "S":
            return True
        case "N":
            return False
        case _:
            print("opcao invalida digite novamente: [S/N]")
            return True


while start:
    n = int(input("Digite um numero: "))
    numeros.append(n)
    opt = str(input("quer continuar? [S/N]").upper())
    start = escolha(opt)
    numeros.sort()

for i in numeros:
    if i % 2 == 0:
        pares.append(i)
        pares.sort()
    else:
        impares.append(i)
        impares.sort()
print(numeros)
print(pares)
print(impares)
