from random import randint
from time import sleep


def dado(i):
    match i:
        case 0:
            d1 = randint(0, 20)
            return d1
        case 1:
            d2 = randint(0, 20)
            return d2
        case 2:
            d3 = randint(0, 20)
            return d3
        case 3:
            d4 = randint(0, 20)
            return d4


dados = dict()

for i in range(4):
    if i == 0:
        dados["jogador 01"] = dado(i)
    elif i == 1:
        dados["jogador 02"] = dado(i)
    elif i == 2:
        dados["jogador 03"] = dado(i)
    elif i == 3:
        dados["jogador 04"] = dado(i)


for k, v in dados.items():
    print(f"O {k} tirou {v}")
    sleep(1)


vencedor = max(dados.values())

for k, v in dados.items():
    if vencedor == v:
        print(f"O vencedor foi o jogador {k} tirando: {v}")
