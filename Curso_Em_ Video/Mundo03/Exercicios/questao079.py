numeros = []
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
    count += 1
    numeros.sort()

ternario = "sim" if 5 in numeros else "Nao"

print(
    f"foram digitados {count} o valor 5 esta na lista? {ternario} a lista ordenado fica assim: {numeros}"
)
