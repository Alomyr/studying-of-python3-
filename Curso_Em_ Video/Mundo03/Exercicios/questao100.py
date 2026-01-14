from random import randint
from time import sleep

numeros = []


def sortear(lista):
    print("Os numeros sorteados foram:")
    for i in range(5):
        n = randint(0, 10)
        print(n, end="-", flush=True)
        sleep(0.5)
        lista.append(n)
    print(f"A lista dos numero sorteados ficou assim: {lista}")


def soma_de_pares(lista):
    somarPares = 0
    print("Esses sao os numeros pares")
    for i in lista:
        if i % 2 == 0:
            print(i, end=",", flush=True)
            sleep(0.5)
            somarPares += i
    print(f"a soma dos numeros pares resultou em: {somarPares}")


sortear(numeros)
soma_de_pares(numeros)
