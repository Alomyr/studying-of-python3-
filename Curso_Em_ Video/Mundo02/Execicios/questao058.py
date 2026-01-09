from curses import init_pair
import random

incio = 0
fim = 11
numeros = list(range(incio, fim))

random.shuffle(numeros)

while True:
    escolha = int(
        input(
            "Nesse jogo vc precisa adivinhar em qual numero de 0 a 10 eu estou pensando\nDigite um numero: "
        )
    )
    print("voltei")
    if escolha == numeros[0]:
        print("Vc venceu")
        break
    else:
        print("Vc perdeu o numero era")
