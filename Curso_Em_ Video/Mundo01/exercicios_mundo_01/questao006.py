# programa que calcula o dubro, triplo e a raiz quadrada de um numero

numero = float(input("Digite um numero: "))
dobro = numero * 2
triplo = numero * 3
raiz = numero**0.5

print(
    "Para o numero: {}, seu sobro é {} o seu triplo é {} e sua raiz quadrada é {}".format(
        numero, dobro, triplo, raiz
    )
)
