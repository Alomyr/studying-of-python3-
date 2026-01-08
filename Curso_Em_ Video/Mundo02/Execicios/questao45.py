# game jokenpo
from random import randint
from time import sleep

pc = randint(0, 2)
jogada = int(
    input(
        """oq vc quer jogar
                   [1] pedra
                   [2] papel
                   [3] tesoura """
    )
)
item = ["pedra", "papel", "tesoura"]


print("Jo")
sleep(1)
print("ken")
sleep(1)
print("po!")

print("vc escolheu: {} e o pc escoheu : {}".format(item[jogada], item[pc]))

if pc == jogada:
    print("empate")
elif pc == 0:
    if jogada == 1:
        print("jogador win")
    else:
        print("jogador louse")
elif pc == 1:
    if jogada == 2:
        print("jogador win")
    else:
        print("jogador louse")
else:
    if jogada == 0:
        print("jogador win")
    else:
        print("jogador louse")
