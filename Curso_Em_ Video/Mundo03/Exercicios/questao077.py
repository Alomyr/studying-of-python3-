numeros = []
start = True


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
    if not (n in numeros):
        numeros.append(n)
    else:
        print(f"Esse valor {n} ja existe na lista\n digite outro valor")
    opt = str(input("quer continuar? [S/N]").upper())
    start = escolha(opt)
print(numeros)
