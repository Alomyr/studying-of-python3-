import random

start = True
cont = 0


def escolhas(opt):
    match opt:
        case 1:
            return "Par"
        case 2:
            return "Impar"


opt = int(input("vc quer ser par ou impa ?\n[1] Par          [2] Impar: "))
escolha = escolhas(opt)

while start:
    if escolha == "Par":
        numeroJogador = int(input("Digite o numero q vc quer jogar: "))
        soma = numeroJogador + random.randint(0, 10)
        if soma % 2 == 0:
            print(f"o resultado de {soma} vc venceu")
            cont += 1
        else:
            print(f"o resultado de {soma} vc perdeu")
            start = False

    elif escolha == "Impar":
        numeroJogador = input("Digite o numero q vc quer jogar: ")
        soma = numeroJogador + random.randint(0, 10)
        if soma % 2 == 1:
            print(f"o resultado de {soma} vc venceu")
            cont += 1

        else:
            print(f"o resultado de {soma} vc perdeu")
            start = False
    else:
        start = False

print(f"Vc venceu {cont} vezes esse jogo para bens")
