import random

incio = 0
fim = 6
numeros = list(range(incio, fim))
random.shuffle(numeros)

escolha = int(
    input(
        "Nesse jogo vc precisa adivinhar em qual numero de 0 a 5 eu estou pensando\nDigite um numero: "
    )
)
if escolha == numeros[0]:
    print("Vc venceu")
else:
    print("Vc perdeu o numero era {}".format(numeros[0]))
