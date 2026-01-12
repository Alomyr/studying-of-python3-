lista = list()
menosPesados = list()
maisPesados = list()
start = True
count = 0
maior = 0
menor = 0


def escolha(opt):
    match opt:
        case "S":
            return True
        case "N":
            return False
        case _:
            print("Opcao invalida digite novamente: [S/N] ")
            return True


while start:

    nome = str(input("Digite um nome: "))
    peso = float(input(f"Digite o peso de {nome}: "))
    lista.append([nome, peso])

    opt = str(input("deseja continuar? [S/N] ")).upper()
    start = escolha(opt)

    count += 1

    if len(lista) == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso


print(f"O numero de pessoas cadastras foram: {count}")

for i in range(0, len(lista), 1):
    if lista[i][1] == maior:
        maisPesados.append(lista[i])
    if lista[i][1] == menor:
        menosPesados.append(lista[i])

print(f"o maior peso e de {maior} das pessoas ", end="")

for i in maisPesados:
    print(i[0], end=" ")


print(f"\no menor peso e de {menor} das pessoas ", end="")
for i in menosPesados:
    print(i[0], end=" ")
